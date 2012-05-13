from collections import deque
import time
import logging

from arrange_base import ArrangeBase



class ArrangeSingleWindow(ArrangeBase):
    """ Class to arrange a single window """

    def do(self, geometries):
        """ Main function that performs the arrangement """

        def similar_geometries(ga, gb):
            for i in range(4):
                if abs(ga[i] - gb[i]) >= self.window_geometry_error_margin:
                    return False
            return True
     
        window_original_geometry = self._screen.get_active_window_geometry()

        current_monitor = self._screen.get_active_window_monitor()
        logging.debug("Window currently on monitor {}".format(current_monitor))

        #not an arrangement, but a list of geometires for that matter
        geometries_numeric = self.single_window_positions(geometries, current_monitor)
       
        # Calculate which geometry is the next one to use
        i = 1
        geometry_to_use_index = 0    
        for geometry_numeric in geometries_numeric:
            if similar_geometries(geometry_numeric, window_original_geometry):
                geometry_to_use_index = i % len(geometries_numeric)
                break
            i += 1 

        # Now move the window
        self._screen.move_active_window(geometries_numeric[geometry_to_use_index])


