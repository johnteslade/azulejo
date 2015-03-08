# This file is part of azulejo
#
# Author: Pedro
#
# This code takes care of setting up or loading configurations.
#

import json
import os.path

class AzulejoConfiguration(object):
    """ Handles configuration of program """

    def __init__(self, always_use_initial=False):

        self._initial_config_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'initial_config.json')

        if always_use_initial:
            conf_filename = self._initial_config_path
        else:
            conf_filename = os.path.expanduser('~/.azulejorc.js')

            if not os.path.isfile(conf_filename):
                print("Creating file: '%s'" % (conf_filename))
                self.create_initial_config_file(conf_filename)

        print("Reading config file: '%s'" % (conf_filename))
        json_string = self.read_file(conf_filename)

        self.conf_data = json.loads(json_string)

    @staticmethod
    def read_file(path):
        """Returns file content as string."""
        file_handler = open(path, 'r')
        content = file_handler.read()
        file_handler.close()
        return content


    def create_initial_config_file(self, conf_filename):
        """Create a file with config values."""
        with open(conf_filename, 'w') as cfgfile:
            raw_json = self.read_file(self._initial_config_path)
            cfgfile.write(raw_json)

    def get_config_data(self):
        """ Gets the config data """
        return self.conf_data


