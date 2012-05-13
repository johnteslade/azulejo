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
               'monitor': 0,
           },
           {
               'geometry': [ 200, 0, 5, 5 ],
               'active': False,
               'monitor': 0,
           },
           {
               'geometry': [ 200, 0, 5, 5 ],
               'active': False,
               'monitor': 0,
           },
           {
               'geometry': [ 200, 0, 5, 5 ],
               'active': False,
               'monitor': 0,
           },
        ]

