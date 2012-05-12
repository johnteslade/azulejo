import gtk
import keybinder
import configuration

from azulejo_controller import AzulejoController


def dispatcher(dis_param):
    
    (func, azulejo_obj, param) = dis_param

    azulejo_obj.force_update()
    func(azulejo_obj, param)    
    
    
def run():    

    azulejo_obj = AzulejoController()

    for action in configuration.conf_data:
        
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
