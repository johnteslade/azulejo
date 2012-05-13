import logging
import unittest
from mock import patch
import keybinder
import azulejo_screen
import gtk
import azulejo

from test.screen_mocks import SingleTestScreenMock
from test.key_binder import KeyBinderDummy


class AzulejoTest(unittest.TestCase):

    def test_left_side(self):
        """ Test the left side moving of windows """  
        
        keybinding_obj = KeyBinderDummy()

        screen = SingleTestScreenMock()

        # Run the code under test
        azulejo.run(True, screen, keybinding_obj)

        # Trigger a keypress
        keybinding_obj.action_key('<Super>h')

        self.assertEqual(
            screen.get_active_window()['geometry'],
            [0, 0, 1000, 1000]
        )
        
        # Trigger another keypress
        keybinding_obj.action_key('<Super>h')

        self.assertEqual(
            screen.get_active_window()['geometry'],
            [0, 0, 600, 1000]
        )
        
        # Trigger another keypress
        keybinding_obj.action_key('<Super>h')

        self.assertEqual(
            screen.get_active_window()['geometry'],
            [0, 0, 1400, 1000]
        )


    def test_maximise(self):
        """ Test the maximising of active window """  
        
        keybinding_obj = KeyBinderDummy()

        screen = SingleTestScreenMock()

        # Run the code under test
        azulejo.run(True, screen, keybinding_obj)

        # Trigger a keypress
        keybinding_obj.action_key('<Super>1')

        self.assertEqual(
            screen.get_active_window()['geometry'],
            [0, 0, 2000, 1000]
        )
        

    def test_side_by_side(self):
        """ Test the side by side windows """  
        
        keybinding_obj = KeyBinderDummy()

        screen = SingleTestScreenMock()

        # Run the code under test
        azulejo.run(True, screen, keybinding_obj)

        # Trigger a 2 window side by side
        keybinding_obj.action_key('<Super>2')

        self.assertEqual(
            screen.windows[0]['geometry'],
            [0, 0, 1000, 1000]
        )

        self.assertEqual(
            screen.windows[1]['geometry'],
            [1001, 0, 1000, 1000]
        )
        
        # Trigger a 3 window side by side
        keybinding_obj.action_key('<Super>3')

        self.assertEqual(
            screen.windows[0]['geometry'],
            [0, 0, 1000, 1000]
        )

        self.assertEqual(
            screen.windows[1]['geometry'],
            [1001, 0, 1000, 500]
        )

        self.assertEqual(
            screen.windows[2]['geometry'],
            [1001, 501, 1000, 500]
        )
       
        # Trigger a 4 window side by side
        keybinding_obj.action_key('<Super>4')

        self.assertEqual(
            screen.windows[0]['geometry'],
            [0, 0, 1000, 500]
        )

        self.assertEqual(
            screen.windows[1]['geometry'],
            [1001, 0, 1000, 500]
        )

        self.assertEqual(
            screen.windows[2]['geometry'],
            [0, 501, 1000, 500]
        )

        self.assertEqual(
            screen.windows[3]['geometry'],
            [1001, 501, 1000, 500]
        )



if __name__ == '__main__':
    unittest.main()



