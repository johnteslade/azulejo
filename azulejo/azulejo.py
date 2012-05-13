import gtk
import keybinder
import configuration
import logging

from azulejo_controller import AzulejoController
from configuration import AzulejoConfiguration

def dispatcher(dis_param):
    
    (func, azulejo_obj, param) = dis_param

    azulejo_obj.force_update()
    func(azulejo_obj, param) 

        
def run(test=False):    

    azulejo_obj = AzulejoController()

    logging.basicConfig(level=logging.DEBUG)

    for action in AzulejoConfiguration(test).get_config_data():
        
        keybinder.bind(
            action['keybind'], 
            dispatcher, 
            (
                azulejo_obj.get_action_function(action['function']), 
                azulejo_obj, 
                action['parameters']
            )
        )        

    # Detect if we are testing
    if test:

        # Special bind to pass out the main object for testing
        # This is a little messy - TODO work out best way for this
        keybinder.bind(
            'all', 
            None, 
            azulejo_obj 
        )  

    else:
        # Main loop for gtk
        gtk.main()



