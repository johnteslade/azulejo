from .arrange_base import ArrangeBase



class ArrangeMultipleWindows(ArrangeBase):
    """ Class to arrange multiple windows """

    def do(self, arrangement):
        """ Main function that performs the arrangement """
        self._screen.move_windows(
            self.get_possible_positions(arrangement)
        )
