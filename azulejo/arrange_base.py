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


    def do(self, params):
        """ Main function that performs the arrangement """

        raise NotImplementedError


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
        
        return [ self.create_geometry(position, monitor) for position in positions ] 



