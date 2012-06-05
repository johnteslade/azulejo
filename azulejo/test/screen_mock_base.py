


class ScreenMockBase:
    """ Base mock object for the screen """

    monitor_geometry = []
    windows = []

    def __init__(self):
        raise NotImplementedError

    
    def get_all_windows(self):
        """ Gets all windows in the screen """

        return self.windows

    
    def get_monitor_geometry(self, monitor=None):
        """ Returns a rectangle with geometry of the specified monitor """

        return self.monitor_geometry[monitor]


    def get_active_window(self):
        """ Returns the active window """

        active_windows = filter(lambda x: x['active'] == True, self.windows)
        assert len(active_windows) == 1

        return active_windows[0]


    def get_active_window_monitor(self):
        """ Returns the monitor of the currently active window """

        for x in xrange(len(self.monitor_geometry)):

            monitor = self.monitor_geometry[x]
            window = self.get_active_window()['geometry']

            if (window[0] >= monitor.x) and (window[0] < monitor.x + monitor.width) and (window[1] >= monitor.y) and (window[1] < monitor.y + monitor.height):
                return x
       
        # If we get here then we have a mismatch between windows and monitors
        raise RuntimeError


    def get_active_window_geometry(self):
        """ Returns the geometry of the current active window """

        return self.get_active_window()['geometry']


    def move_active_window(self, new_geometry):
        """ Moves the active window the specified geometry """
        
        for x in xrange(len(self.windows)):
            if self.windows[x]['active']:
                self.windows[x]['geometry'] = new_geometry
                break
    

    def move_windows(self, new_geometry_list):
        """ Moves the active window the specified geometry """
        
        for x in xrange(len(new_geometry_list)):
            self.windows[x]['geometry'] = new_geometry_list[x]


    def maximise_active_window(self):
        """ Maximises the active window """ 

        monitor_size = self.get_monitor_geometry(self.get_active_window_monitor())
        self.move_active_window([monitor_size.x, monitor_size.y, monitor_size.width, monitor_size.height])

    
    def get_number_monitors(self):
        """ Returns the number of monitors in use """

        return len(self.monitor_geometry)

   
    def get_width(self):
        """ Returns width of screen """
       
        # TODO not useful for multimonitor
        return self.monitor_geometry[0].width 


    def get_height(self):
        """ Returns height of screen """
        
        # TODO not useful for multimonitor
        return self.monitor_geometry[0].height


    def update(self):
        """ Forces and update """

        # Nothing to do in the mock
        pass

