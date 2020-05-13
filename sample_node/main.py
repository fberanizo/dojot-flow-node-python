# -*- coding: utf-8 -*-
import os
from dojot_flow_node import DojotHandler, DataHandlerBase


class DataHandler(DataHandlerBase):

    def get_node_representation_path(self):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sample.html')
    
    def get_locale_data(self):
        # This is just a sample copied over from node-red-contrib-rpe, as a sample
        # A real implementation might want to parse the contents off a file
        return {}

    def get_metadata(self):
        return {
            # ID can actually be any unique human-friendly string
            # on proper node-red modules it is "$module/$name"
            'id': 'sample/kelvin',
            # This is usually the name of the node
            'name': 'kelvin',
            # This is usually the name of the node
            'module': 'kelvin',
            'version': '0.0.0',
        }

    def handle_message(self, config, message, metadata):
        celcius = self._get(config['in'], message)
        self._set(config['out'], celcius + 273.15, message)
        return [message]


if __name__ == '__main__':
    DojotHandler(DataHandler())
