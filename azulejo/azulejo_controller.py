from collections import deque
import time
import logging

from azulejo_screen import AzulejoScreen
from arrange_base import ArrangeBase
from arrange_single_window import ArrangeSingleWindow
from arrange_maximize import ArrangeMaximize
from arrange_move_monitor import ArrangeMoveMonitor
from arrange_multiple_windows import ArrangeMultipleWindows
from arrange_rotate import ArrangeRotate



class AzulejoController:

    def __init__(self):
        """ Initialiser """

        self._screen = AzulejoScreen() # Main screen object

        #because window resizing is not acurate we need a quick dirty workaround
        self.window_geometry_error_margin = 30

        #variable to hold the amount of windows since the last arrangement
        self.arrangement_size = 0

        self.arrange_base = ArrangeBase(self._screen)

        self._action_classes = {
            'resize_single_window': ArrangeSingleWindow(self._screen),
            'resize_windows': ArrangeMultipleWindows(self._screen),
            'rotate_windows': ArrangeRotate(self._screen),
            'maximize': ArrangeMaximize(self._screen),     
            'move_monitor': ArrangeMoveMonitor(self._screen),       
        }


    def do_action(self, function, params):
        """ Returns the function for a given action """

        # Force screen update
        self._screen.update()
        
        # Call the correct function
        self._action_classes[function].do(params)



