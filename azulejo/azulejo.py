import logging

from .azulejo_controller import AzulejoController
from .configuration import AzulejoConfiguration

def dispatcher(dis_param):
    """ A dispatcher used for key binding """

    (azulejo_obj, function, params) = dis_param

    azulejo_obj.do_action(function, params)


def run(test=False, screen_obj=None, keybinder_obj=None):
    """ Main entry point of code """

    azulejo_obj = AzulejoController(screen_obj)

    logging.basicConfig(level=logging.DEBUG)

    if keybinder_obj == None:
        import keybinder
        keybinder_obj = keybinder

    for action in AzulejoConfiguration(test).get_config_data():


        logging.info("Binding action {} to keys {}".format(action['name'], action['keybind']))

        for key in action['keybind']:
            keybinder_obj.bind(
                key,
                dispatcher,
                (
                    azulejo_obj,
                    action['function'],
                    action['parameters']
                )
            )

    # Main loop for gtk
    if not test:
        import gtk
        gtk.main()



