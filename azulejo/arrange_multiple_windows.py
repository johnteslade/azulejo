from collections import deque
import time
import logging

from arrange_base import ArrangeBase



class ArrangeMultipleWindows(ArrangeBase):
    """ Class to arrange multiple windows """

    def do(self, arrangement):
        """ Main function that performs the arrangement """

        # TODO this does not work across multiple monitors well

        self._screen.move_windows(
            self.parse_arrangement(arrangement)
        )


