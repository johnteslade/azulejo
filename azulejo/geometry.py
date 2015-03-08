

class Geometry(object):
    """ A class to hold the geometry of a window or screen """

    def __init__(self, x=None, y=None, width=None, height=None):

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def _as_list(self):
        """ Returns the class a list [x, y, width, height] """

        return [self.x, self.y, self.width, self.height]


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


import nose.tools
class TestGeometry(object):

    def test_equal(self):
        """Test equality of objects."""

        a = Geometry(1, 1, 2, 2)
        b = Geometry(1, 1, 2, 2)
        c = Geometry(4, 4, 5, 5)

        nose.tools.assert_equal(a, b)
        nose.tools.assert_not_equal(id(a), id(b))
        nose.tools.assert_not_equal(a, c)
        nose.tools.assert_not_equal(b, c)

    def test_similar(self):
        """Test object similarity."""

        a = Geometry(0, 0, 100, 100)
        b = Geometry(0, 0, 80, 80)

        nose.tools.assert_not_equal(a, b)
        nose.tools.assert_true(a.is_similar(b))
        nose.tools.assert_false(a.is_similar(b, error_margin=20))
        nose.tools.assert_false(a.is_similar(b, error_margin=10))

