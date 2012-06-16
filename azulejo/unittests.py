import logging
import unittest
from mock import patch
import keybinder
import azulejo_screen
import gtk
import azulejo

from test.screen_mocks import SingleTestScreenMock
from test.screen_mocks import MultipleTestScreenMock
from test.key_binder import KeyBinderDummy


class AzulejoTestBase(unittest.TestCase):
    """ Base setup of tests """
    
    @classmethod
    def setUpClass(self):
        """ Constructor """
        self.screen = None
        self.keybinding_obj = None


class AzulejoTestSingle(AzulejoTestBase):
    """ Test cases for single monitor setup """

    def setUp(self):
        """ Setup and start azulejo """
        pass

    def test_left_side(self):
        """ Test the left side moving of windows """  
        
        self.keybinding_obj = KeyBinderDummy()

        self.screen = SingleTestScreenMock()

        # Run the code under test
        azulejo.run(True, self.screen, self.keybinding_obj)

        # Trigger a keypress
        self.keybinding_obj.action_key('<Ctrl><Super>h')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            [0, 0, 1000, 1000]
        )
        
        # Trigger another keypress
        self.keybinding_obj.action_key('<Ctrl><Super>h')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            [0, 0, 600, 1000]
        )
        
        # Trigger another keypress
        self.keybinding_obj.action_key('<Ctrl><Super>h')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            [0, 0, 1400, 1000]
        )


    def test_maximise(self):
        """ Test the maximising of active window """  
        
        self.keybinding_obj = KeyBinderDummy()

        self.screen = SingleTestScreenMock()

        # Run the code under test
        azulejo.run(True, self.screen, self.keybinding_obj)

        # Trigger a keypress
        self.keybinding_obj.action_key('<Ctrl><Super>1')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            [0, 0, 2000, 1000]
        )
        

    def test_side_by_side_2(self):
        """ Test the side by side 2 windows """  
        
        self.keybinding_obj = KeyBinderDummy()

        self.screen = SingleTestScreenMock()

        # Run the code under test
        azulejo.run(True, self.screen, self.keybinding_obj)

        # Trigger a 2 window side by side
        self.keybinding_obj.action_key('<Ctrl><Super>2')

        self.assertEqual(
            self.screen.windows[0]['geometry'],
            [0, 0, 1000, 1000]
        )

        self.assertEqual(
            self.screen.windows[1]['geometry'],
            [1001, 0, 1000, 1000]
        )


    def test_side_by_side_3(self):
        """ Test the side by side 3 windows """  
        
        self.keybinding_obj = KeyBinderDummy()

        self.screen = SingleTestScreenMock()

        # Run the code under test
        azulejo.run(True, self.screen, self.keybinding_obj)

        # Trigger a 3 window side by side
        self.keybinding_obj.action_key('<Ctrl><Super>3')

        self.assertEqual(
            self.screen.windows[0]['geometry'],
            [0, 0, 1000, 1000]
        )

        self.assertEqual(
            self.screen.windows[1]['geometry'],
            [1001, 0, 1000, 500]
        )

        self.assertEqual(
            self.screen.windows[2]['geometry'],
            [1001, 501, 1000, 500]
        )
      

    def test_side_by_side_4(self):
        """ Test the side by side 4 windows """  
        
        self.keybinding_obj = KeyBinderDummy()

        self.screen = SingleTestScreenMock()

        # Run the code under test
        azulejo.run(True, self.screen, self.keybinding_obj) 

        # Trigger a 4 window side by side
        self.keybinding_obj.action_key('<Ctrl><Super>4')

        self.assertEqual(
            self.screen.windows[0]['geometry'],
            [0, 0, 1000, 500]
        )

        self.assertEqual(
            self.screen.windows[1]['geometry'],
            [1001, 0, 1000, 500]
        )

        self.assertEqual(
            self.screen.windows[2]['geometry'],
            [0, 501, 1000, 500]
        )

        self.assertEqual(
            self.screen.windows[3]['geometry'],
            [1001, 501, 1000, 500]
        )


    def test_move_window(self):
        """ Test the moving of a window on the self.screen """  
        
        self.keybinding_obj = KeyBinderDummy()

        self.screen = SingleTestScreenMock()

        # Run the code under test
        azulejo.run(True, self.screen, self.keybinding_obj)

        # Move northwest
        self.keybinding_obj.action_key('<Super>KP_7')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            [0, 0, 50, 100]
        )
        
        # Move southeast
        self.keybinding_obj.action_key('<Super>KP_3')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            [1950, 900, 50, 100]
        )   
 

class AzulejoTestMultiple(AzulejoTestBase):
    """ Test cases for multi monitor setup """

    def test_left_side_multiple(self):
        """ Test the left side moving of windows when multiple monitors are in place """  
        
        self.keybinding_obj = KeyBinderDummy()

        self.screen = MultipleTestScreenMock()

        # Run the code under test
        azulejo.run(True, self.screen, self.keybinding_obj)

        # Trigger a keypress
        self.keybinding_obj.action_key('<Ctrl><Super>h')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            [200, 0, 100, 100]
        )


    def test_move_monitor(self):
        """ Test the moving of window to a monitor """  
        
        self.keybinding_obj = KeyBinderDummy()

        self.screen = MultipleTestScreenMock()

        # Run the code under test
        azulejo.run(True, self.screen, self.keybinding_obj)

        self.assertEqual(self.screen.get_active_window_monitor(), 1)

        # Move left
        self.keybinding_obj.action_key('<Ctrl><Super>q')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            [50, 10, 20, 30]
        )
        
        self.assertEqual(self.screen.get_active_window_monitor(), 0)

        # Move right
        self.keybinding_obj.action_key('<Ctrl><Super>w')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            [250, 10, 20, 30]
        )
        
        self.assertEqual(self.screen.get_active_window_monitor(), 1)
    
    
    def test_move_monitor_maximise(self):
        """ Test the moving of window to a monitor and maximise """  
        
        self.keybinding_obj = KeyBinderDummy()

        self.screen = MultipleTestScreenMock()

        # Run the code under test
        azulejo.run(True, self.screen, self.keybinding_obj)

        self.assertEqual(self.screen.get_active_window_monitor(), 1)

        # Move left
        self.keybinding_obj.action_key('<Ctrl><Super>a')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            [0, 0, 200, 100]
        )
       
        self.assertEqual(self.screen.get_active_window_monitor(), 0)
        
        # Move right
        self.keybinding_obj.action_key('<Ctrl><Super>s')
        
        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            [200, 0, 200, 100]
        )
        
        self.assertEqual(self.screen.get_active_window_monitor(), 1)


    def test_move_window_multi_monitor(self):
        """ Test the moving of a window on the self.screen when using multiple monitors"""  
        
        self.keybinding_obj = KeyBinderDummy()

        self.screen = MultipleTestScreenMock()

        # Run the code under test
        azulejo.run(True, self.screen, self.keybinding_obj)

        # Move northwest
        self.keybinding_obj.action_key('<Super>KP_7')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            [200, 0, 20, 30]
        )
        
        # Move southeast
        self.keybinding_obj.action_key('<Super>KP_3')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            [380, 70, 20, 30]
        )    


if __name__ == '__main__':

    unittest.TextTestRunner(verbosity=2).run(
        unittest.TestSuite([
            unittest.TestLoader().loadTestsFromTestCase(AzulejoTestSingle),
            unittest.TestLoader().loadTestsFromTestCase(AzulejoTestMultiple),
        ])
    )
