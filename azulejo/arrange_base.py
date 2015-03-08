import logging

from .geometry import Geometry

class ArrangeBase(object):
    """ A base class for defining an action to arrange window(s) """

    def __init__(self, screen_in):
        """ Initialiser """

        self._screen = screen_in # Main screen object

        #variable to hold the amount of windows since the last arrangement
        self.arrangement_size = 0


    def do(self, params):
        """ Main function that performs the arrangement """

        raise NotImplementedError


    def parse_simple_math_expressions(self, expression, subst_vars):
        """ Parses the string expression and evaluates it """

        expression = str(expression)

        for subst in subst_vars.keys():
            expression = expression.replace(subst, str(subst_vars[subst]))

        return int(eval(expression))


    def create_geometry(self, geometry_in, monitor):
        """ Creates the geometry for the config input """

        monitor_geometry = self._screen.get_monitor_geometry(monitor)

        # Parse the string values coming in
        geometry_out_list = [ self.parse_simple_math_expressions(coord, { 'w': monitor_geometry.width, 'h': monitor_geometry.height} ) for coord in geometry_in ]

        # Create final geometry (account for the x and y of the monitor)
        geometry_out = Geometry(
            x=geometry_out_list[0] + monitor_geometry.x,
            y=geometry_out_list[1] + monitor_geometry.y,
            width=geometry_out_list[2],
            height=geometry_out_list[3]
        )

        logging.debug("Possible geometry = {}".format(geometry_out))

        return geometry_out


    def get_possible_positions(self, positions, monitor=None):
        """ Function to create all possible window positions  """

        return [ self.create_geometry(position, monitor) for position in positions ]



