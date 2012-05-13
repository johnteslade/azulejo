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

        
def run(main=True):    

    azulejo_obj = AzulejoController()

    logging.basicConfig(level=logging.DEBUG)

    for action in AzulejoConfiguration(True).get_config_data():
        
        keybinder.bind(
            action['keybind'], 
            dispatcher, 
            (
                azulejo_obj.get_action_function(action['function']), 
                azulejo_obj, 
                action['parameters']
            )
        )        

    if main:
        gtk.main()



