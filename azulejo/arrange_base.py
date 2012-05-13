from collections import deque
import time
import logging

from azulejo_screen import AzulejoScreen



class ArrangeBase:
    """ A base class for defining an action to arrange window(s) """    

    def __init__(self, screen_in):
        """ Initialiser """

        self._screen = screen_in # Main screen object

        #because window resizing is not acurate we need a quick dirty workaround
        self.window_geometry_error_margin = 30

        #variable to hold the amount of windows since the last arrangement
        self.arrangement_size = 0


    def parse_simple_math_expressions(self, expression, width=None, height=None):
        """ Parses the string expression and evaluates it """
        
        expression = str(expression)
        
        if width == None:
            width = self._screen.get_width() 
            
        if height == None:
            height = self._screen.get_height() 
            
        expression = expression.replace('w', str(width))
        expression = expression.replace('h', str(height))

        return int(eval(expression))

    
    def parse_geometry(self, geometry):
        return map(self.parse_simple_math_expressions, geometry)



    def parse_arrangement(self, arrangement):
        return map(self.parse_geometry, arrangement)

    
    def create_geometry(self, geometry_in, monitor):
        """ Creates the geometry for the config input """
      
        monitor_geometry = self._screen.get_monitor_geometry(monitor) 

        # Parse the string values coming in
        geometry_out = [ self.parse_simple_math_expressions(coord, monitor_geometry.width, monitor_geometry.height) for coord in geometry_in ]

        # Modify the geometry to account for the x and y of the monitor
        geometry_out[0] += monitor_geometry.x
        geometry_out[1] += monitor_geometry.y
        
        logging.debug("Possible geometry = {}".format(geometry_out))

        return geometry_out


    def single_window_positions(self, positions, monitor):
        """ Function to create all possible window positions 
        
        currently separate while multi-monitor is being added """

        all_positions = []

        for position in positions:
            all_positions.append(
                self.create_geometry(position, monitor)
            )

        return all_positions


    def resize_windows(self, arrangement):
        """ Resizes multiple windows """

        self._screen.move_windows(
            self.parse_arrangement(arrangement)
        )


    def resize_single_window(self, geometries):
        """ Resizes just a single window """

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


    def rotate_windows(self, dummy):
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

    def maximize(self, dummy):
        """ Maximise window """

        self._screen.maximise_active_window()



