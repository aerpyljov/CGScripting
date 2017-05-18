#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtGui import *
import settings, createProject
import os


class ProjectListClass(QListWidget):
    def __init__(self):
        super(ProjectListClass, self).__init__()

    def update_project_list(self):
        data = settings.SettingsClass().load()
        path = data.get('path')
        if path:
            if os.path.exists(path):
                for f in os.listdir(path):
                    fullPath = os.path.join(path, f)
                    if self.isProject(fullPath):
                        self.addProject(f)
            return True
        else:
            return False

    def isProject(self, path):
        return os.path.exists(os.path.join(path, createProject.projectFile))

    def addProject(self, name):
        item = QListWidgetItem()
        item.setText(name)
        self.addItem(item)

