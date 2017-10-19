#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
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
        app_folder = os.path.dirname(os.path.abspath(__file__))
        path_folder = os.path.join(app_folder, 'PROJECTS')
        archive_folder = os.path.join(app_folder, 'ARCHIVE')
        backup_folder = os.path.join(app_folder, 'BACKUP')
        for folder in (path_folder, archive_folder, backup_folder):
            if not os.path.exists(folder):
                os.mkdir(folder)
        def_data = dict(
            path=path_folder,
            archive=archive_folder,
            backup=backup_folder,
            winEncoding='cp1251'
        )
        with open(path, 'w') as f:
            json.dump(def_data, f, indent=4)

    def load(self):
        return json.load(open(self.path))

    def save(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4)
