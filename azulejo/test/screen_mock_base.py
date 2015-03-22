

class ScreenMockBase(object):
    """ Base mock object for the screen """

    monitor_geometry = []
    windows = []

    def get_all_windows(self):
        """ Gets all windows in the screen """
        return self.windows

    def get_all_window_monitors(self):
        """Get all windows, geometry and monitor.

        Returns list of tuple window_obj, geometry, monitor.
        """
        output = []
        for win in self.windows:
            output.append((win, win['geometry'], self.get_window_monitor(win['geometry'])))
        return output


    def get_monitor_geometry(self, monitor=None):
        """Returns a rectangle with geometry of the specified monitor.

        If no monitor uses one with active window.
        """
        if monitor == None:
            monitor = self.get_active_window_monitor()

        return self.monitor_geometry[monitor]


    def get_active_window(self):
        """ Returns the active window """
        return self.windows[0]

    def get_active_window_monitor(self):
        """ Returns the monitor of the currently active window """
        return self.get_window_monitor(self.get_active_window_geometry())

    def get_window_monitor(self, window):
        """Return the monitor of the window."""

        for x, monitor in enumerate(self.monitor_geometry):

            if (window.x >= monitor.x) \
                    and (window.x < monitor.x + monitor.width) \
                    and (window.y >= monitor.y) \
                    and (window.y < monitor.y + monitor.height):
                return x

        # If we get here then we have a mismatch between windows and monitors
        raise RuntimeError

    def get_active_window_geometry(self):
        """ Returns the geometry of the current active window """

        return self.get_active_window()['geometry']


    def move_active_window(self, new_geometry):
        """ Moves the active window the specified geometry """

        self.windows[0]['geometry'] = new_geometry


    def move_windows(self, new_geometry_list, reverse=False):
        """ Moves the active window the specified geometry """

        for x in range(len(new_geometry_list)):
            if new_geometry_list[x]:
                self.windows[x]['geometry'] = new_geometry_list[x]


    def maximise_active_window(self):
        """ Maximises the active window """

        monitor_size = self.get_monitor_geometry(
            self.get_active_window_monitor())
        self.move_active_window(monitor_size)


    def get_number_monitors(self):
        """ Returns the number of monitors in use """

        return len(self.monitor_geometry)


    def update(self):
        """ Forces and update """

        # Nothing to do in the mock
        pass

