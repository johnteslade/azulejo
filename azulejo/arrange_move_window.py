from collections import deque
import time
import logging

from arrange_base import ArrangeBase



class ArrangeMoveWindow(ArrangeBase):
    """ Class to move a single window around the screen """

    def do(self, geometries):
        """ Main function that performs the arrangement """

        window_original_geometry = self._screen.get_active_window_geometry()
        current_monitor_geometry = self._screen.get_monitor_geometry(self._screen.get_active_window_monitor())

        logging.debug("Original window {}".format(window_original_geometry))

        window_width = window_original_geometry[2]
        window_height = window_original_geometry[3]
        screen_width = current_monitor_geometry[2]
        screen_height = current_monitor_geometry[3]
        
        new_geometry = [
            current_monitor_geometry[0] + eval(geometries[0]), 
            current_monitor_geometry[1] + eval(geometries[1]),
            window_original_geometry[2],
            window_original_geometry[3]
        ]

        # Now move the window
        logging.debug("Moving window to {}".format(new_geometry))
        self._screen.move_active_window(new_geometry)


