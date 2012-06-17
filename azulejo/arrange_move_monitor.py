from collections import deque
import time
import logging

from arrange_base import ArrangeBase
from geometry import Geometry



class ArrangeMoveMonitor(ArrangeBase):
    """ Class to move a window to another monitor """

    def do(self, params):
        """ Main function that performs the arrangement """
       
        direction = params[0]       
        resize = params[1]       

        # No action if only one monitor
        if self._screen.get_number_monitors() == 1:
            return

        old_monitor = self._screen.get_active_window_monitor()
        old_monitor_geometry = self._screen.get_monitor_geometry(old_monitor) 
        
        logging.debug("Window currently on monitor {}.  Moving {}".format(old_monitor, direction))

        new_monitor = old_monitor

        # Work out if we have a new monitor number
        if direction == "left":
            if old_monitor > 0:
                new_monitor = old_monitor - 1
        else:
            if old_monitor < self._screen.get_number_monitors() - 1:
                new_monitor = old_monitor + 1

        # Do we need to move the window?
        if new_monitor != old_monitor:

            window_original_geometry = self._screen.get_active_window_geometry()
            new_monitor_geometry = self._screen.get_monitor_geometry(new_monitor) 

            # TODO deal with if the window is now too large for the new monitor
            new_position = Geometry(
                x=new_monitor_geometry.x + (window_original_geometry[0] - old_monitor_geometry.x),
                y=new_monitor_geometry.y + (window_original_geometry[1] - old_monitor_geometry.y),
                width=window_original_geometry[2], 
                height=window_original_geometry[3], 
            )
            
            logging.debug("Moving to monitor {} and geometry {}".format(new_monitor, new_position))

            # Now move the window
            self._screen.move_active_window(new_position)

            # Maximise the window if required
            if resize == "max":
                logging.debug("Maximising window")
                self._screen.maximise_active_window()

            

