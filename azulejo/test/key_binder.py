


class KeyBinderDummy:
    """ Class this is used to allow keybindings to be caught and to be actioned """

    def __init__(self):
    
        self.bindings = []
        self.saved_obj = None


    def bind(self, action, dispatcher, dispatcher_params):
        """ Bind a key press """

        if action == 'all':
            # Detect special all binding as being the controller
            self.saved_obj = dispatcher_params
        else:
            self.bindings.append({
                'action': action,
                'dispatcher': dispatcher,
                'dispatcher_params': dispatcher_params,
            })
        
    def action_key(self, action):
        """ Actions a key press by calling the relavent dispatcher """

        key_found = filter(lambda x: x['action'] == action, self.bindings)
        assert len(key_found) == 1
        func = key_found[0]['dispatcher']
        func(key_found[0]['dispatcher_params'])

    def get_screen(self):
        """ Get's the screen object """
        
        return self.saved_obj._screen
