# coding: utf-8

import json


class ConfigGetter(object):

    def __init__(self, hostname):
        self.data_path = self.get_data_path(hostname)
        self.model_path = self.get_model_path(hostname)

    def get_data_path(self, hostname):
        f = open("./config/config.json", 'r')
        json_data = json.load(f)
        return json_data[hostname]['data_path']

    def get_model_path(self, hostname):
        f = open("./config/config.json", 'r')
        json_data = json.load(f)
        return json_data[hostname]['model_path']