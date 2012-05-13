from collections import deque
import time
import logging

from arrange_base import ArrangeBase



class ArrangeRotate(ArrangeBase):
    """ Class to rotate through windows """

    def do(self, dummy):
        """ Main function that performs the arrangement """

        windows = self._screen.get_all_windows()
        amount_of_windows = len(windows)
        
        if amount_of_windows > self.arrangement_size:
            windows = windows[:self.arrangement_size]
            
        geos = []
        for window in windows:
            window_geo = window.get_geometry()
            window_geo = window_geo[:4]
            geos.append(window_geo)
            
            #do the actual rotations, lets use deque as it's dramatically more efficient than a trivial shift implementation
        windows_deq = deque(windows)
        windows_deq.rotate(1)
          
        rotation_len = len(windows_deq)
        i = 0
        while i < rotation_len:
            geometry_list_args = [0, 255]
            index = rotation_len - (i + 1) #again, start by the tail
            geometry_list_args.extend(map (int, geos[index]))
            windows_deq[index].unmaximize()
            windows_deq[index].set_geometry(*geometry_list_args)
            i += 1
        
        #(windows_deq[0]).activate(int(time.time())) #not sure why it doesn't work. if uncommented causes other windows beyond the rotated ones to hide behind current ones even after pressing ctrl+tab


