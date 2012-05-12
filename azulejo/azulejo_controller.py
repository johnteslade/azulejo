from collections import deque
import time

from azulejo_screen import AzulejoScreen



class AzulejoController:

    def __init__(self):
        """ Initialiser """

        self._screen = AzulejoScreen() # Main screen object

        #because window resizing is not acurate we need a quick dirty workaround
        self.window_geometry_error_margin = 30

        #variable to hold the amount of windows since the last arrangement
        self.arrangement_size = 0


    def parse_simple_math_expressions(self, expression):
        expression = str(expression)
        expression = expression.replace('w', str(self._screen.get_width()))
        expression = expression.replace('h', str(self._screen.get_height()))
        return eval(expression)

        

    def parse_geometry(self, geometry):
        return map(self.parse_simple_math_expressions, geometry)



    def parse_arrangement(self, arrangement):
        return map(self.parse_geometry, arrangement)


    def single_window_positions(self, positions):
        """ Function to create all possible window positions 
        
        currently separate while multi-monitor is being added """

        all_positions = []

        for position in positions:
            all_positions.append(
                [ self.parse_simple_math_expressions(coord) for coord in position ]
            )

        return all_positions


    def resize_windows(self, arrangement):
        arrangement_numeric = self.parse_arrangement(arrangement)
        #print arrangement_numeric
        filtered_windows = self._screen.get_all_windows()
        amount_of_windows = len(filtered_windows)     
        
        if amount_of_windows < len(arrangement_numeric):
            arrangement_numeric = arrangement_numeric[:amount_of_windows]
      
        i = 0
        self.arrangement_size = len(arrangement_numeric) #global scope variable, also used to rotate windows
        while i < self.arrangement_size:
            geometry_list_args = [0, 255]
            index = self.arrangement_size - (i + 1) #we must start in the end in order to keep window order correct
            geometry_list_args.extend(map (int, arrangement_numeric[index]))
            filtered_windows[index].unmaximize()
            filtered_windows[index].set_geometry(*geometry_list_args)
            i += 1



    def resize_single_window(self, geometries):

        def similar_geometries(ga, gb):
            for i in range(4):
                if abs(ga[i] - gb[i]) >= self.window_geometry_error_margin:
                    return False
            return True
     
        window = self._screen.get_active_window()    
        window_original_geometry = window.get_geometry()

        #not an arrangement, but a list of geometires for that matter
        geometries_numeric = self.single_window_positions(geometries)
        geometry_list_args = [0, 255]
        
        i = 1
        geometry_to_use_index = 0    
        for geometry_numeric in geometries_numeric:
            if similar_geometries(geometry_numeric, window_original_geometry):
                geometry_to_use_index = i % len(geometries_numeric)
                break
            i += 1 

        geometry_list_args.extend(map (int, geometries_numeric[geometry_to_use_index]))
        window.unmaximize()
        window.set_geometry(*geometry_list_args)




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
        windows = self._screen.get_all_windows()
        curwin = windows[0]
        curwin.maximize()

    def force_update(self):
        """ Forces update on screen """

        self._screen.update()


    def get_action_function(self, action):
        """ Returns the function for a given action """
        return self._callable_actions[action]

    _callable_actions = dict(\
        resize_single_window=resize_single_window, \
        resize_windows=resize_windows, \
        rotate_windows=rotate_windows, \
        maximize=maximize        
    )

