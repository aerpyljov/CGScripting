#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtGui import *
from widgets import projectManager_UI as ui, projectListWidget


class ProjectManagerClass(QMainWindow, ui.Ui_projectManager):
    def __init__(self):
        super(ProjectManagerClass, self).__init__()
        self.setupUi(self)
        # widgets
        self.projectList_lwd = projectListWidget.ProjectListClass()
        self.projectList_ly.addWidget(self.projectList_lwd)
        # connects
        self.create_btn.clicked.connect(self.create_project)
        self.settings_btn.clicked.connect(self.open_settings_dialog)
        self.templateEditor_btn.clicked.connect(self.open_template_editor_dialog)

    def update_list(self):
        pass

    def open_settings_dialog(self):
        pass

    def open_template_editor_dialog(self):
        pass

    def create_project(self):
        pass

    def show_info(self):
        pass


if __name__ == '__main__':
    app = QApplication([])
    w = ProjectManagerClass()
    w.show()
    app.exec_()
