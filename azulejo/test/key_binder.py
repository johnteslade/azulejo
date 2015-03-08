


class KeyBinderDummy(object):
    """Class used to allow keybindings to be caught and to be actioned."""

    def __init__(self):

        self.bindings = []
        self.saved_obj = None


    def bind(self, action, dispatcher, dispatcher_params):
        """ Bind a key press """

        self.bindings.append({
            'action': action,
            'dispatcher': dispatcher,
            'dispatcher_params': dispatcher_params,
        })


    def action_key(self, action):
        """ Actions a key press by calling the relavent dispatcher """

        key_found = [x for x in self.bindings if x['action'] == action]
        assert len(key_found) == 1
        func = key_found[0]['dispatcher']
        func(key_found[0]['dispatcher_params'])


