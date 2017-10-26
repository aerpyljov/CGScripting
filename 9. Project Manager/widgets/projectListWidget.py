#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtGui import *
from PySide.QtCore import *
import settings, createProject
import os


class ProjectListClass(QListWidget):

    itemDroppedSignal = Signal(object)
    itemDraggedSignal = Signal(object)

    def __init__(self):
        super(ProjectListClass, self).__init__()
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
        self.itemDroppedSignal.emit(event)

    def startDrag(self, dropAction):
        self.itemDraggedSignal.emit(dropAction)

    def dragEnterEvent(self, event):
        """Called when the cursor gets to the area first"""
        if event.source() is self:  # Forbid dropping on the same widget
            event.ignore()
        else:
            mimedata = event.mimeData()
            if mimedata.hasUrls():
                event.accept()
            else:
                event.ignore()

    def dragMoveEvent(self, event):
        """Called many times while the cursor moving"""
        if event.source() is self:  # Forbid dropping on the same widget
            event.ignore()
        else:
            mimedata = event.mimeData()
            if mimedata.hasUrls():  # How does the cursor look?
                event.accept()
            else:
                event.ignore()