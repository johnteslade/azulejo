import logging
import unittest
from mock import patch
import keybinder
import azulejo_screen
import gtk

from test.screen_mocks import SingleTestScreenMock
from test.key_binder import KeyBinderDummy



class AzulejoTest(unittest.TestCase):

    @patch.object(keybinder, 'bind')
    def test_left_side(self, mock_my_method):
        """ Test the left side moving of windows """  
        
        keybinding_obj = KeyBinderDummy()

        # Defined sideeffect for the key bind operation
        def side_effect(key, dispatcher, dispatcher_params):
            keybinding_obj.bind(key, dispatcher, dispatcher_params)
        mock_my_method.side_effect = side_effect

        # Monkey patch
        azulejo_screen.AzulejoScreen = SingleTestScreenMock

        # Import and run the code under test
        import azulejo
        azulejo.run(True)

        # Trigger a keypress
        keybinding_obj.action_key('<Super>h')

        self.assertEqual(
            keybinding_obj.get_screen().get_active_window()['geometry'],
            [0, 0, 1000, 1000]
        )
        
        # Trigger another keypress
        keybinding_obj.action_key('<Super>h')

        self.assertEqual(
            keybinding_obj.get_screen().get_active_window()['geometry'],
            [0, 0, 600, 1000]
        )
        
        # Trigger another keypress
        keybinding_obj.action_key('<Super>h')

        self.assertEqual(
            keybinding_obj.get_screen().get_active_window()['geometry'],
            [0, 0, 1400, 1000]
        )


    @patch.object(keybinder, 'bind')
    def test_maximise(self, mock_my_method):
        """ Test the maximising of active window """  
        
        keybinding_obj = KeyBinderDummy()

        # Defined sideeffect for the key bind operation
        def side_effect(key, dispatcher, dispatcher_params):
            keybinding_obj.bind(key, dispatcher, dispatcher_params)
        mock_my_method.side_effect = side_effect

        # Monkey patch
        azulejo_screen.AzulejoScreen = SingleTestScreenMock

        # Import and run the code under test
        import azulejo
        azulejo.run(True)

        # Trigger a keypress
        keybinding_obj.action_key('<Super>1')

        self.assertEqual(
            keybinding_obj.get_screen().get_active_window()['geometry'],
            [0, 0, 2000, 1000]
        )
        

    @patch.object(keybinder, 'bind')
    def test_side_by_side(self, mock_my_method):
        """ Test the side by side windows """  
        
        keybinding_obj = KeyBinderDummy()

        # Defined sideeffect for the key bind operation
        def side_effect(key, dispatcher, dispatcher_params):
            keybinding_obj.bind(key, dispatcher, dispatcher_params)
        mock_my_method.side_effect = side_effect

        # Monkey patch
        azulejo_screen.AzulejoScreen = SingleTestScreenMock

        # Import and run the code under test
        import azulejo
        azulejo.run(True)

        # Trigger a 2 window side by side
        keybinding_obj.action_key('<Super>2')

        self.assertEqual(
            keybinding_obj.get_screen().windows[0]['geometry'],
            [0, 0, 1000, 1000]
        )

        self.assertEqual(
            keybinding_obj.get_screen().windows[1]['geometry'],
            [1001, 0, 1000, 1000]
        )
        
        # Trigger a 3 window side by side
        keybinding_obj.action_key('<Super>3')

        self.assertEqual(
            keybinding_obj.get_screen().windows[0]['geometry'],
            [0, 0, 1000, 1000]
        )

        self.assertEqual(
            keybinding_obj.get_screen().windows[1]['geometry'],
            [1001, 0, 1000, 500]
        )

        self.assertEqual(
            keybinding_obj.get_screen().windows[2]['geometry'],
            [1001, 501, 1000, 500]
        )
       
        # Trigger a 4 window side by side
        keybinding_obj.action_key('<Super>4')

        self.assertEqual(
            keybinding_obj.get_screen().windows[0]['geometry'],
            [0, 0, 1000, 500]
        )

        self.assertEqual(
            keybinding_obj.get_screen().windows[1]['geometry'],
            [1001, 0, 1000, 500]
        )

        self.assertEqual(
            keybinding_obj.get_screen().windows[2]['geometry'],
            [0, 501, 1000, 500]
        )

        self.assertEqual(
            keybinding_obj.get_screen().windows[3]['geometry'],
            [1001, 501, 1000, 500]
        )



if __name__ == '__main__':
    unittest.main()



