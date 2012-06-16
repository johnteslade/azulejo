from collections import deque
import logging
import time

from arrange_maximize import ArrangeMaximize
from arrange_move_monitor import ArrangeMoveMonitor
from arrange_move_window import ArrangeMoveWindow
from arrange_multiple_windows import ArrangeMultipleWindows
from arrange_rotate import ArrangeRotate
from arrange_single_window import ArrangeSingleWindow
from azulejo_screen import AzulejoScreen



class AzulejoController:

    def __init__(self, screen_obj_in):
        """ Initialiser """

        # Set the main screen object
        if screen_obj_in:
            self._screen = screen_obj_in
        else:
            self._screen = AzulejoScreen()

        self._action_classes = {
            'maximize': ArrangeMaximize(self._screen),     
            'move_monitor': ArrangeMoveMonitor(self._screen),       
            'move_single_window': ArrangeMoveWindow(self._screen),       
            'resize_single_window': ArrangeSingleWindow(self._screen),
            'resize_windows': ArrangeMultipleWindows(self._screen),
            'rotate_windows': ArrangeRotate(self._screen),
        }


    def do_action(self, function, params):
        """ Returns the function for a given action """

        # Force screen update
        self._screen.update()
       
        logging.debug("--- Starting action {}".format(function))

        # Call the correct function
        self._action_classes[function].do(params)
        
        logging.debug("--- Action done {}".format(function))



