import logging
import unittest
from mock import patch
import azulejo_screen
import azulejo

from test.screen_mocks import SingleTestScreenMock
from test.screen_mocks import MultipleTestScreenMock
from test.key_binder import KeyBinderDummy
from geometry import Geometry


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
        
        self.keybinding_obj = KeyBinderDummy()
        self.screen = SingleTestScreenMock()

        azulejo.run(True, self.screen, self.keybinding_obj)


    def test_left_side(self):
        """ Test the left side moving of windows """  
        
        # Trigger a keypress
        self.keybinding_obj.action_key('<Ctrl><Super>h')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            Geometry(x=0, y=0, width=1000, height=1000)
        )
        
        # Trigger another keypress
        self.keybinding_obj.action_key('<Ctrl><Super>h')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            Geometry(x=0, y=0, width=600, height=1000)
        )
        
        # Trigger another keypress
        self.keybinding_obj.action_key('<Ctrl><Super>h')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            Geometry(x=0, y=0, width=1400, height=1000)
        )


    def test_maximise(self):
        """ Test the maximising of active window """  
        
        # Trigger a keypress
        self.keybinding_obj.action_key('<Ctrl><Super>1')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            Geometry(x=0, y=0, width=2000, height=1000)
        )
        

    def test_side_by_side_2(self):
        """ Test the side by side 2 windows """  
        
        # Trigger a 2 window side by side
        self.keybinding_obj.action_key('<Ctrl><Super>2')

        self.assertEqual(
            self.screen.windows[0]['geometry'],
            Geometry(x=0, y=0, width=1000, height=1000)
        )

        self.assertEqual(
            self.screen.windows[1]['geometry'],
            Geometry(x=1001, y=0, width=1000, height=1000)
        )


    def test_side_by_side_3(self):
        """ Test the side by side 3 windows """  
        
        # Trigger a 3 window side by side
        self.keybinding_obj.action_key('<Ctrl><Super>3')

        self.assertEqual(
            self.screen.windows[0]['geometry'],
            Geometry(x=0, y=0, width=1000, height=1000)
        )

        self.assertEqual(
            self.screen.windows[1]['geometry'],
            Geometry(x=1001, y=0, width=1000, height=500)
        )

        self.assertEqual(
            self.screen.windows[2]['geometry'],
            Geometry(x=1001, y=501, width=1000, height=500)
        )
      

    def test_side_by_side_4(self):
        """ Test the side by side 4 windows """  
        
        # Trigger a 4 window side by side
        self.keybinding_obj.action_key('<Ctrl><Super>4')

        self.assertEqual(
            self.screen.windows[0]['geometry'],
            Geometry(x=0, y=0, width=1000, height=500)
        )

        self.assertEqual(
            self.screen.windows[1]['geometry'],
            Geometry(x=1001, y=0, width=1000, height=500)
        )

        self.assertEqual(
            self.screen.windows[2]['geometry'],
            Geometry(x=0, y=501, width=1000, height=500)
        )

        self.assertEqual(
            self.screen.windows[3]['geometry'],
            Geometry(x=1001, y=501, width=1000, height=500)
        )


    def test_move_window(self):
        """ Test the moving of a window on the self.screen """  
        
        # Move northwest
        self.keybinding_obj.action_key('<Super>KP_7')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            Geometry(x=0, y=0, width=50, height=100)
        )
        
        # Move southeast
        self.keybinding_obj.action_key('<Super>KP_3')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            Geometry(x=1950, y=900, width=50, height=100)
        )   

    def test_multiple_window_moves(self):
        """ Tests multiple window moves """  
        
        # Move side by side
        self.keybinding_obj.action_key('<Ctrl><Super>2')

        self.assertEqual(
            self.screen.get_all_windows()[0]['geometry'],
            Geometry(x=0, y=0, width=1000, height=1000)
        )

        self.assertEqual(
            self.screen.get_all_windows()[1]['geometry'],
            Geometry(x=1001, y=0, width=1000, height=1000)
        )

        # Move 4 pain
        self.keybinding_obj.action_key('<Ctrl><Super>4')

        self.assertEqual(
            self.screen.get_all_windows()[0]['geometry'],
            Geometry(x=0, y=0, width=1000, height=500)
        )

        self.assertEqual(
            self.screen.get_all_windows()[1]['geometry'],
            Geometry(x=1001, y=0, width=1000, height=500)
        ) 

        self.assertEqual(
            self.screen.get_all_windows()[2]['geometry'],
            Geometry(x=0, y=501, width=1000, height=500)
        )

        self.assertEqual(
            self.screen.get_all_windows()[3]['geometry'],
            Geometry(x=1001, y=501, width=1000, height=500)
        ) 


class AzulejoTestMultiple(AzulejoTestBase):
    """ Test cases for multi monitor setup """

    def setUp(self):
        """ Setup and start azulejo """
        
        self.keybinding_obj = KeyBinderDummy()
        self.screen = MultipleTestScreenMock()

        azulejo.run(True, self.screen, self.keybinding_obj)


    def test_left_side_multiple(self):
        """ Test the left side moving of windows when multiple monitors are in place """  
        
        # Trigger a keypress
        self.keybinding_obj.action_key('<Ctrl><Super>h')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            Geometry(x=200, y=0, width=100, height=100)
        )


    def test_move_monitor(self):
        """ Test the moving of window to a monitor """  
        
        self.assertEqual(self.screen.get_active_window_monitor(), 1)

        # Move left
        self.keybinding_obj.action_key('<Ctrl><Super>q')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            Geometry(x=50, y=10, width=20, height=30)
        )
        
        self.assertEqual(self.screen.get_active_window_monitor(), 0)

        # Move right
        self.keybinding_obj.action_key('<Ctrl><Super>w')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            Geometry(x=250, y=10, width=20, height=30)
        )
        
        self.assertEqual(self.screen.get_active_window_monitor(), 1)
    
    
    def test_move_monitor_maximise(self):
        """ Test the moving of window to a monitor and maximise """  
        
        self.assertEqual(self.screen.get_active_window_monitor(), 1)

        # Move left
        self.keybinding_obj.action_key('<Ctrl><Super>a')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            Geometry(x=0, y=0, width=200, height=100)
        )
       
        self.assertEqual(self.screen.get_active_window_monitor(), 0)
        
        # Move right
        self.keybinding_obj.action_key('<Ctrl><Super>s')
        
        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            Geometry(x=200, y=0, width=200, height=100)
        )
        
        self.assertEqual(self.screen.get_active_window_monitor(), 1)


    def test_move_window_multi_monitor(self):
        """ Test the moving of a window on the self.screen when using multiple monitors"""  
        
        # Move northwest
        self.keybinding_obj.action_key('<Super>KP_7')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            Geometry(x=200, y=0, width=20, height=30)
        )
        
        # Move southeast
        self.keybinding_obj.action_key('<Super>KP_3')

        self.assertEqual(
            self.screen.get_active_window()['geometry'],
            Geometry(x=380, y=70, width=20, height=30)
        )   


    def test_multiple_window_moves_multi_monitor(self):
        """ Tests multiple window moves from multiple monitors """  
        
        # Move side by side
        self.keybinding_obj.action_key('<Ctrl><Super>2')

        self.assertEqual(
            self.screen.get_all_windows()[0]['geometry'],
            Geometry(x=200, y=0, width=100, height=100)
        )

        self.assertEqual(
            self.screen.get_all_windows()[1]['geometry'],
            Geometry(x=301, y=0, width=100, height=100)
        )

        # Move 4 pain
        self.keybinding_obj.action_key('<Ctrl><Super>4')

        self.assertEqual(
            self.screen.get_all_windows()[0]['geometry'],
            Geometry(x=200, y=0, width=100, height=50)
        )

        self.assertEqual(
            self.screen.get_all_windows()[1]['geometry'],
            Geometry(x=301, y=0, width=100, height=50)
        ) 

        self.assertEqual(
            self.screen.get_all_windows()[2]['geometry'],
            Geometry(x=200, y=51, width=100, height=50)
        )

        self.assertEqual(
            self.screen.get_all_windows()[3]['geometry'],
            Geometry(x=301, y=51, width=100, height=50)
        ) 


if __name__ == '__main__':

    unittest.TextTestRunner(verbosity=2).run(
        unittest.TestSuite([
            unittest.TestLoader().loadTestsFromTestCase(AzulejoTestSingle),
            unittest.TestLoader().loadTestsFromTestCase(AzulejoTestMultiple),
        ])
    )
