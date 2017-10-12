#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtGui import *
from PySide.QtCore import *
import settings, createProject
import os


class DropNotifier(QObject):
    itemDropped = Signal(object)

    def __init__(self):
        QObject.__init__(self)

    def emit_signal(self, event):
        self.itemDropped.emit(event)

class ProjectListClass(QListWidget):
    def __init__(self):
        super(ProjectListClass, self).__init__()
        self.drop_notifier = DropNotifier()

        # ui
        self.sortItems(Qt.AscendingOrder)
        self.setSortingEnabled(True)

    def update_project_list(self):
        self.clear()
        data = settings.SettingsClass().load()
        path = data.get('path')
        if path:
            if os.path.exists(path):
                for f in os.listdir(path):
                    fullPath = os.path.join(path, f)
                    if self.isProject(fullPath):
                        item = self.addProject(f)
                        item.setData(32, fullPath)
            return True
        else:
            return False

    def isProject(self, path):
        return os.path.exists(os.path.join(path, createProject.projectFile))

    def addProject(self, name):
        item = QListWidgetItem()
        item.setText(name)
        self.addItem(item)
        return item

    def dropEvent(self, event):
        self.drop_notifier.emit_signal(event)
