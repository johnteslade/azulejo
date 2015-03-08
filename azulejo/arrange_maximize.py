from collections import deque
import time
import logging

from .arrange_base import ArrangeBase



class ArrangeMaximize(ArrangeBase):
    """ Class to maximize a single window """

    def do(self, dummy):
        """ Main function that performs the arrangement """

        self._screen.maximise_active_window()


