#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

settingsFileName = 'ProjectManagerSettings.json'
settingsFolder = os.path.expanduser('~')


class SettingsClass(object):
    def __init__(self):
        self.path = os.path.join(settingsFolder, settingsFileName)
        if not os.path.exists(self.path):
            self.make_default(self.path)

    @staticmethod
    def make_default(path):
        def_data = dict(
            path=''
        )
        with open(path, 'w') as f:
            json.dump(def_data, f, indent=4)

    def load(self):
        return json.load(open(self.path))

    def save(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4)
