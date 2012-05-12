import wnck
import gtk


class AzulejoScreen:
    """ 
    
    Class to hold details of the current screen 
    
    This it to partially remove the direct dependency on gtk in the main class (potentially easier to test) 

    """

    def __init__(self):
        """ Initialiser """
        
        self.maximized_window_geometry = gtk.gdk.get_default_root_window().property_get('_NET_WORKAREA')[2][:4]
        self.upper_corner = self.maximized_window_geometry[:2]


    def get_all_windows(self):
        """ Gets all windows in the screen """

        def f_normal_window(window):
            if window.get_window_type() == wnck.WindowType.__enum_values__[0]:
                return True
            return False

        s = wnck.screen_get_default()

        while gtk.events_pending():
            gtk.main_iteration()

        windows = s.get_windows_stacked()
        filtered_windows = filter(f_normal_window, windows)
        filtered_windows.reverse()
        return filtered_windows

    def get_active_window(self):
        """ Returns the active window """

        return wnck.screen_get_default().get_active_window()


    def get_active_window_geometry(self):
        """ Returns the geometry of the current active window """

        return wnck.screen_get_default().get_active_window().get_geometry()


    def move_active_window(self, new_geometry):
        """ Moves the active window the specified geometry """
        
        geometry_list_args = [0, 255]
        window = wnck.screen_get_default().get_active_window()    
        geometry_list_args.extend(map (int, new_geometry))
        window.unmaximize()
        window.set_geometry(*geometry_list_args)


    def update(self):
        """ Forces and update """

        # Doesn't appear to do much
        wnck.screen_get_default().force_update()


    

    def get_width(self):
        """ Returns width of screen """
        
        return self.maximized_window_geometry[2] 


    def get_height(self):
        """ Returns height of screen """
        
        return self.maximized_window_geometry[3] 





