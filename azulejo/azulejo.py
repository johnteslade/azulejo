import gtk
import keybinder
import configuration

from azulejo_controller import AzulejoController
from configuration import AzulejoConfiguration

def dispatcher(dis_param):
    
    (func, azulejo_obj, param) = dis_param

    azulejo_obj.force_update()
    func(azulejo_obj, param)    
    
    
def run():    

    azulejo_obj = AzulejoController()

    for action in AzulejoConfiguration().get_config_data():
        
        keybinder.bind(
            action['keybind'], 
            dispatcher, 
            (
                azulejo_obj.get_action_function(action['function']), 
                azulejo_obj, 
                action['parameters']
            )
        )        

    gtk.main()
