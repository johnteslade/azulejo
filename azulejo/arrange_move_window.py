from collections import deque
import time
import logging

from arrange_base import ArrangeBase
from geometry import Geometry



class ArrangeMoveWindow(ArrangeBase):
    """ Class to move a single window around the screen """

    def do(self, geometries):
        """ Main function that performs the arrangement """

        window_original_geometry = self._screen.get_active_window_geometry()
        current_monitor_geometry = self._screen.get_monitor_geometry(self._screen.get_active_window_monitor())

        logging.debug("Original window {}".format(window_original_geometry))

        subst_vars = {
            'window_width': window_original_geometry[2],
            'window_height': window_original_geometry[3],
            'screen_width': current_monitor_geometry[2],
            'screen_height': current_monitor_geometry[3],
        }

        new_geometry = Geometry(
            x=current_monitor_geometry[0] + self.parse_simple_math_expressions(geometries[0], subst_vars), 
            y=current_monitor_geometry[1] + self.parse_simple_math_expressions(geometries[1], subst_vars),
            width=window_original_geometry[2],
            height=window_original_geometry[3]
        )

        # Now move the window
        logging.debug("Moving window to {}".format(new_geometry))
        self._screen.move_active_window(new_geometry)


