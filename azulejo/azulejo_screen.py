import gtk
import wnck

from .geometry import Geometry


class AzulejoScreen(object):
    """
    Class to hold details of the current screen

    This is to encapsulate the gtk that actually communicates with the system.
    This will allow us to change libraries if needed and also allows the
    creation of a mock screen object for testing.

    """

    def __init__(self):
        """ Initialiser """
        pass

    @staticmethod
    def get_all_windows():
        """Get all windows in the screen."""

        # Get screen - this must come before gtk loop
        screen = wnck.screen_get_default()

        # Deal with pending events
        while gtk.events_pending():
            gtk.main_iteration()

        # Get windows list and filter for normal windows
        windows = screen.get_windows_stacked()
        filtered_windows = [
            window for window in windows
            if window.get_window_type() == wnck.WindowType.__enum_values__[0]]
        filtered_windows.reverse()
        return filtered_windows

    def get_all_window_monitors(self):
        """Get all windows, geometry and monitor.

        Returns list of tuple window_obj, geometry, monitor.
        """
        output = []
        windows = self.get_all_windows()
        for win in windows:
            output.append((win, self.get_window_geometry(win), self.get_window_monitor(win)))
        return output

    def get_monitor_geometry(self, monitor=None):
        """Return a rectangle with geometry of the specified monitor.

        If no monitor uses one with active window.
        """
        if monitor is None:
            monitor = self.get_active_window_monitor()

        return gtk.gdk.screen_get_default().get_monitor_geometry(monitor)

    @staticmethod
    def get_active_window():
        """ Returns the active window """
        return wnck.screen_get_default().get_active_window()


    def get_window_monitor(self, window):
        """ Returns the monitor of the currently active window """

        # Find the window coordinates then find out which monitor this is
        active_window_geo = self.get_window_geometry(window)
        return gtk.gdk.screen_get_default().get_monitor_at_point(
            active_window_geo.x, active_window_geo.y)

    def get_active_window_monitor(self):
        """ Returns the monitor of the window """

        return self.get_window_monitor(self.get_active_window())

    @staticmethod
    def get_window_geometry(window):
        """ Returns the geometry of the window """

        geometry = window.get_geometry()
        return Geometry(
            x=geometry[0], y=geometry[1],
            width=geometry[2], height=geometry[3]
        )

    def get_active_window_geometry(self):
        """ Returns the geometry of the current active window """

        return self.get_window_geometry(self.get_active_window())


    def move_active_window(self, new_geometry):
        """ Moves the active window """

        self.move_window(
            wnck.screen_get_default().get_active_window(), new_geometry)


    def move_windows(self, new_geometry_list, reverse=False):
        """ Moves a number of windows - starting from the active """

        filtered_windows = self.get_all_windows()

        if reverse:
            window_indexes = range(len(new_geometry_list) - 1, 0, -1)
        else:
            window_indexes = range(len(new_geometry_list))

        for x in window_indexes:
            if x < len(filtered_windows) and new_geometry_list[x]:
                self.move_window(filtered_windows[x], new_geometry_list[x])

    @staticmethod
    def move_window(window, new_geometry):
        """ Moves the window to the specified geometry """

        geometry_list_args = [0, 255] + \
            [
                new_geometry.x, new_geometry.y,
                new_geometry.width, new_geometry.height
            ]
        window.unmaximize()
        window.set_geometry(*geometry_list_args)


    def maximise_active_window(self):
        """ Maximises the active window """

        windows = self.get_all_windows()
        curwin = windows[0]
        curwin.maximize()


    @staticmethod
    def get_number_monitors():
        """ Returns the number of monitors in use """

        return gtk.gdk.screen_get_default().get_n_monitors()


    @staticmethod
    def update():
        """ Forces and update """

        # Doesn't appear to do much
        wnck.screen_get_default().force_update()



