#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
from PySide.QtGui import *
from widgets import projectManager_UI as ui, projectListWidget
import settingsDialog, createProjectDialog, templateEditor, settings, createProject
import webbrowser

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
        self.projectList_lwd.itemClicked.connect(self.show_info)
        self.projectList_lwd.itemDoubleClicked.connect(self.openProject)

        # start
        self.update_list()
        self.info_lb.setText('')

    def update_list(self):
        if not self.projectList_lwd.update_project_list():
            self.create_btn.setEnabled(0)
        else:
            self.create_btn.setEnabled(1)

    def open_settings_dialog(self):
        # Modal window
        self.dial = settingsDialog.SettingsDialogClass(self)
        if self.dial.exec_():
            data = self.dial.get_table_data()
            settings.SettingsClass().save(data)
        self.update_list()

    def open_template_editor_dialog(self):
        # Modeless window
        self.dial = templateEditor.TemplateEditorClass()
        self.dial.show()

    def create_project(self):
        # Modal window
        self.dial = createProjectDialog.CreateProjectDialogClass(self)
        if self.dial.exec_():
            data = self.dial.getDialogData()
            createProject.createProject(data)
            self.update_list()

    def show_info(self, item):
        info = createProject.getProjectInfo(item.data(32))
        if info:
            text = """Name:
{0}

Comment:
{1}
""".format(info['name'], info['comment'])
        else:
            text = ''
        self.info_lb.setText(text)

    def openProject(self, item):
        path = item.data(32)
        webbrowser.open(path)


if __name__ == '__main__':
    app = QApplication([])
    w = ProjectManagerClass()
    w.show()
    app.exec_()
