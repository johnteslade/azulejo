from collections import deque
import time
import logging

from azulejo_screen import AzulejoScreen
from arrange_single_window import ArrangeSingleWindow
from arrange_maximize import ArrangeMaximize
from arrange_move_monitor import ArrangeMoveMonitor
from arrange_multiple_windows import ArrangeMultipleWindows
from arrange_rotate import ArrangeRotate



class AzulejoController:

    def __init__(self, screen_obj_in):
        """ Initialiser """

        # Set the main screen object
        if screen_obj_in:
            self._screen = screen_obj_in
        else:
            self._screen = AzulejoScreen()

        #because window resizing is not acurate we need a quick dirty workaround
        self.window_geometry_error_margin = 30

        #variable to hold the amount of windows since the last arrangement
        self.arrangement_size = 0

        self._action_classes = {
            'maximize': ArrangeMaximize(self._screen),     
            'move_monitor': ArrangeMoveMonitor(self._screen),       
            'resize_single_window': ArrangeSingleWindow(self._screen),
            'resize_windows': ArrangeMultipleWindows(self._screen),
            'rotate_windows': ArrangeRotate(self._screen),
        }


    def do_action(self, function, params):
        """ Returns the function for a given action """

        # Force screen update
        self._screen.update()
       
        logging.debug("Starting action {}".format(function))

        # Call the correct function
        self._action_classes[function].do(params)



