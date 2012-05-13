import gtk
import keybinder
import configuration
import logging

from azulejo_controller import AzulejoController
from configuration import AzulejoConfiguration

def dispatcher(dis_param):
    """ A dispatcher used for key binding """

    (azulejo_obj, function, params) = dis_param

    azulejo_obj.do_action(function, params) 

        
def run(test=False):    
    """ Main entry point of code """

    azulejo_obj = AzulejoController()

    logging.basicConfig(level=logging.DEBUG)

    for action in AzulejoConfiguration(test).get_config_data():
        
        keybinder.bind(
            action['keybind'], 
            dispatcher, 
            (
                azulejo_obj, 
                action['function'], 
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



