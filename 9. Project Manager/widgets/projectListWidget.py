#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtGui import *
import settings


class ProjectListClass(QListWidget):
    def __init__(self):
        super(ProjectListClass, self).__init__()

    def update_project_list(self):
        data = settings.SettingsClass().load()
        if data.get('path'):
            return True
        else:
            return False


