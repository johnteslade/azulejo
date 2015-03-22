import logging

from .arrange_move_monitor import ArrangeMonitorBase



class ArrangeSwapMonitor(ArrangeMonitorBase):
    """Class to swap a window with another monitor.

    The current window will be moved to the specified monitor and maximised.
    The first window on the destination monitor will be moved to current
    monitor and maximised.
    """

    def do(self, params):
        """ Main function that performs the arrangement """

        direction = params[0]

        # No action if only one monitor
        if self._screen.get_number_monitors() == 1:
            return

        windows = self._screen.get_all_window_monitors()

        # Monitor A is the one with the current active window
        # Monitor B is who we are swapping with

        monitor_a = self._screen.get_active_window_monitor()
        monitor_b = self.new_monitor(monitor_a, (direction == "left"))

        monitor_a_geometry = self._screen.get_monitor_geometry(monitor_a)
        monitor_b_geometry = self._screen.get_monitor_geometry(monitor_b)

        if monitor_a == monitor_b:
            logging.info("Cannot move this direction")
            return

        print windows

        logging.info("Swapping windows between monitors {} and {}".format(
            monitor_a, monitor_b))

        window_b_index = None

        # Get index into window list for active window on Monitor B
        for x, window in enumerate(windows):
            if window[2] == monitor_b:
                window_b_index = x
                break

        if window_b_index is None:
            logging.info("No window found on Monitor {}".format(monitor_b))
            return

# Keep if we support swapping within maximising
#        window_a_new_geo = self.new_window_geometry(
#            windows[0][1], monitor_a_geometry, monitor_b)
#
#        window_b_new_geo = self.new_window_geometry(
#            windows[window_b_index][1], monitor_b_geometry, monitor_a)

        move_list = [monitor_b_geometry] + \
            [None] * (window_b_index - 1) + \
            [monitor_a_geometry]

        print move_list

        # Move windows
        self._screen.move_windows(move_list, reverse=True)
