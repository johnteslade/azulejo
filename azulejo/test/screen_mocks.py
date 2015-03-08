from screen_mock_base import ScreenMockBase
from azulejo.geometry import Geometry


class SingleTestScreenMock(ScreenMockBase):
    """ Mock for a single screen """

    def __init__(self):

        self.monitor_geometry = [
           Geometry(x=0, y=0, width=2000, height=1000),
        ]

        self.windows = [
           {
               'geometry': Geometry(x=50, y=80, width=50, height=100),
               'active': True,
           },
           {
               'geometry': Geometry(x=200, y=0, width=5, height=5),
               'active': False,
           },
           {
               'geometry': Geometry(x=200, y=0, width=5, height=5),
               'active': False,
           },
           {
               'geometry': Geometry(x=200, y=0, width=5, height=5),
               'active': False,
           },
        ]


class MultipleTestScreenMock(ScreenMockBase):
    """

    Mock for multiple screens

    In a simple side by side configuration where the active window is on the 2nd monitor

    TODO additional types of multiple test config:
        - two monitors arranged top and bottom
        - >2 monitors
        - monitors where one is larger than the other (and moving a too large window to smaller one)

    """

    def __init__(self):

        self.monitor_geometry = [
           Geometry(x=0, y=0, width=200, height=100),
           Geometry(x=200, y=0, width=200, height=100),
        ]

        self.windows = [
           {
               'geometry': Geometry(x=0, y=0, width=10, height=10),
               'active': False,
           },
           {
               'geometry': Geometry(x=100, y=0, width=5, height=5),
               'active': False,
           },
           {
               'geometry': Geometry(x=300, y=0, width=5, height=5),
               'active': False,
           },
           {
               'geometry': Geometry(x=250, y=10, width=20, height=30),
               'active': True,
           },
        ]

