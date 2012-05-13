from collections import deque
import time
import logging

from arrange_base import ArrangeBase



class ArrangeMoveMonitor(ArrangeBase):
    """ Class to move a window to another monitor """

    def do(self, direction):
        """ Main function that performs the arrangement """
       
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
        
            logging.debug("Moving to monitor {}".format(new_monitor))

            window_original_geometry = self._screen.get_active_window_geometry()
            new_monitor_geometry = self._screen.get_monitor_geometry(new_monitor) 

            # TODO deal with if the window is now too large for the new monitor
            new_position = [
                new_monitor_geometry.x + (window_original_geometry[0] - old_monitor_geometry.x),
                new_monitor_geometry.y + (window_original_geometry[1] - old_monitor_geometry.y),
                window_original_geometry[2], 
                window_original_geometry[3], 
            ]
            
            # Now move the window
            self._screen.move_active_window(new_position)


            

