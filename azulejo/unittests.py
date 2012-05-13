import unittest
from mock import patch
import keybinder
import azulejo_screen
import gtk

class AzulejoTest(unittest.TestCase):

    @patch.object(keybinder, 'bind')
    def test_left_side(self, mock_my_method):
        """ Test the left side moving of windows """  
        
        keybinding_obj = KeyBinderDummy()

        # Defined sideeffect for the key bind operation
        def side_effect(key, dispatcher, dispatcher_params):
            keybinding_obj.bind(key, dispatcher, dispatcher_params)
        mock_my_method.side_effect = side_effect

        # Definition of the screen mock for this test
        class SingleTestScreenMock(AzulejoScreenMock):
            def __init__(self):
               
                self.monitor_geometry = [
                   gtk.gdk.Rectangle(x=0, y=0, width=1000, height=1000),
                ]

                self.windows = [
                   {
                       'geometry': [ 0, 0, 10, 10 ],
                       'active': True,
                       'monitor': 0,
                   },
                   {
                       'geometry': [ 200, 0, 5, 5 ],
                       'active': False,
                       'monitor': 0,
                   },
                ]
            


        # Monkey patch
        azulejo_screen.AzulejoScreen = SingleTestScreenMock

        # Import and run the code under test
        import azulejo
        azulejo.run(True)

        # Trigger a keypress
        keybinding_obj.action_key('<Super>h')

        self.assertEqual(
            keybinding_obj.get_screen().get_active_window()['geometry'],
            [0, 0, 500, 1000]
        )
        
        # Trigger another keypress
        keybinding_obj.action_key('<Super>h')

        self.assertEqual(
            keybinding_obj.get_screen().get_active_window()['geometry'],
            [0, 0, 300, 1000]
        )
        
        # Trigger another keypress
        keybinding_obj.action_key('<Super>h')

        self.assertEqual(
            keybinding_obj.get_screen().get_active_window()['geometry'],
            [0, 0, 700, 1000]
        )



class KeyBinderDummy:
    """ Class this is used to allow keybindings to be caught and to be actioned """

    bindings = []
    saved_obj = None

    def __init__(self):

        pass

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


class AzulejoScreenMock:
    """ Mock object for the screen """

    monitor_geometry = []
    windows = []

    def __init__(self):
        raise NotImplementedError

    
    def get_all_windows(self):
        """ Gets all windows in the screen """

        raise NotImplementedError

    
    def get_monitor_geometry(self, monitor=None):
        """ Returns a rectangle with geometry of the specified monitor """

        return self.monitor_geometry[monitor]


    def get_active_window(self):
        """ Returns the active window """

        active_windows = filter(lambda x: x['active'] == True, self.windows)
        assert len(active_windows) == 1

        return active_windows[0]


    def get_active_window_monitor(self):
        """ Returns the monitor of the currently active window """

        return self.get_active_window()['monitor']


    def get_active_window_geometry(self):
        """ Returns the geometry of the current active window """

        return self.get_active_window()['geometry']


    def move_active_window(self, new_geometry):
        """ Moves the active window the specified geometry """
        
        for x in xrange(len(self.windows)):
            if self.windows[x]['active']:
                self.windows[x]['geometry'] = new_geometry
                break
                

    def update(self):
        """ Forces and update """

        # Nothing to do in the mock
        pass


if __name__ == '__main__':
    unittest.main()



