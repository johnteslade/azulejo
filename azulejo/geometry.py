

class Geometry(object):
    """ A class to hold the geometry of a window or screen """

    def __init__(self, x=None, y=None, width=None, height=None):

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def _as_list(self):
        """ Returns the class a list [x, y, width, height] """

        return [ self.x, self.y, self.width, self.height ]


    def is_similar(self, rhs, error_margin=30):
        """ Compare if objects are similar within the given error margin """

        # TODO there might be a neater way to do this

        ga = self._as_list()
        gb = rhs._as_list()

        for i in range(4):
            if abs(ga[i] - gb[i]) >= error_margin:
                return False
        return True


    def __eq__(self, rhs):
        """ Comparison of object using vals """
        return (rhs.x == self.x) and (rhs.y == self.y) and \
            (rhs.width == self.width) and (rhs.height == self.height)

    def __repr__(self):
        return "Geometry(x={}, y={}, width={}, height={})".format(
            self.x, self.y, self.width, self.height)


