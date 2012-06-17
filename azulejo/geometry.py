

class Geometry:
    """ A class to hold the geometry of a window or screen """

    def __init__(self, list_form=None, x=None, y=None, width=None, height=None):
       
        if list_form:
            # TODO get rid of this
            self.x = list_form[0]
            self.y = list_form[1]
            self.width = list_form[2]
            self.height = list_form[3]
        else:
            self.x = x
            self.y = y
            self.width = width
            self.height = height

    def as_list(self):
        """ Returns the class a list [x, y, width, height] """
        return [ self.x, self.y, self.width, self.height ]


    def __getitem__(self, key):

        #raise DeprecationWarning

        # TODO get rid of this eventually

        return self.as_list()[key]
        

    def is_similar(self):
        
        # TODO move ArrangeSingleWindow.similar_geometries and window_geometry_error_margin code here
        
        raise NotImplementedError


    def __cmp__(self, rhs):
        
        if (rhs.x == self.x) and (rhs.y == self.y) and (rhs.width == self.width) and (rhs.height == self.height): 
            return 0
        else:
            return 1

    
    def __repr__(self):
        
        return "Geometry(x={}, y={}, width={}, height={})".format(self.x, self.y, self.width, self.height) 


