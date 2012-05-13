import gtk

from screen_mock_base import ScreenMockBase

class SingleTestScreenMock(ScreenMockBase):
    """ Mock for a single screen """
    
    def __init__(self):
       
        self.monitor_geometry = [
           gtk.gdk.Rectangle(x=0, y=0, width=2000, height=1000),
        ]

        self.windows = [
           {
               'geometry': [ 0, 0, 10, 10 ],
               'active': True,
           },
           {
               'geometry': [ 200, 0, 5, 5 ],
               'active': False,
           },
           {
               'geometry': [ 200, 0, 5, 5 ],
               'active': False,
           },
           {
               'geometry': [ 200, 0, 5, 5 ],
               'active': False,
           },
        ]


class MultipleTestScreenMock(ScreenMockBase):
    """ 
    
    Mock for multiple screens
    
    In a simple side by side configuration where the active screen is on the 2nd monitor

    TODO addition types of multiple test config:
        - two monitors arranged top and bottom
        - >2 monitors
        - monitors where one is larger than the other (and moving a too large window to smaller one)
    
    """
    
    def __init__(self):
       
        self.monitor_geometry = [
           gtk.gdk.Rectangle(x=0, y=0, width=200, height=100),
           gtk.gdk.Rectangle(x=200, y=0, width=200, height=100),
        ]

        self.windows = [
           {
               'geometry': [ 0, 0, 10, 10 ],
               'active': False,
           },
           {
               'geometry': [ 100, 0, 5, 5 ],
               'active': False,
           },
           {
               'geometry': [ 300, 0, 5, 5 ],
               'active': False,
           },
           {
               'geometry': [ 250, 10, 20, 30 ],
               'active': True,
           },
        ]

