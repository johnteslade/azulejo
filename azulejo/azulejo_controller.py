from collections import deque
import time
import logging

from azulejo_screen import AzulejoScreen
from arrange_base import ArrangeBase



class AzulejoController:

    def __init__(self):
        """ Initialiser """

        self._screen = AzulejoScreen() # Main screen object

        #because window resizing is not acurate we need a quick dirty workaround
        self.window_geometry_error_margin = 30

        #variable to hold the amount of windows since the last arrangement
        self.arrangement_size = 0

        self.arrange_base = ArrangeBase(self._screen)

        self._callable_actions = dict(\
            resize_single_window=self.arrange_base.resize_single_window, \
            resize_windows=self.arrange_base.resize_windows, \
            rotate_windows=self.arrange_base.rotate_windows, \
            maximize=self.arrange_base.maximize        
        )


    def do_action(self, function, params):
        """ Returns the function for a given action """

        # Force screen update
        self._screen.update()
        
        # Call the correct function
        func = self._callable_actions[function]
        func(params)



