#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import os, webbrowser, shutil, time, subprocess
from PySide.QtGui import *
from widgets import projectManager_UI as ui, projectListWidget
import settingsDialog, createProjectDialog, templateEditor, settings, createProject, zipfolder


class ProjectManagerClass(QMainWindow, ui.Ui_projectManager):
    def __init__(self):
        super(ProjectManagerClass, self).__init__()
        self.setupUi(self)

        # widgets
        self.projectList_lwd = projectListWidget.ProjectListClass()
        self.projectList_ly.addWidget(self.projectList_lwd)

        # connects
        self.create_btn.clicked.connect(self.create_project)
        self.update_btn.clicked.connect(lambda: self.update_project(self.getFocusedProject()))
        self.refresh_btn.clicked.connect(self.update_list)
        self.settings_btn.clicked.connect(self.open_settings_dialog)
        self.templateEditor_btn.clicked.connect(self.open_template_editor_dialog)
        self.projectList_lwd.itemClicked.connect(self.show_info)
        self.projectList_lwd.itemDoubleClicked.connect(self.openProject)
        self.archive_btn.clicked.connect(lambda: self.archiveProject(self.getFocusedProject()))
        self.backup_btn.clicked.connect(lambda: self.backupProject(self.getFocusedProject()))
        self.openArchive_btn.clicked.connect(lambda: self.openFolder('archive'))
        self.openBackup_btn.clicked.connect(lambda: self.openFolder('backup'))

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

    def update_project(self, item):
        project_path = item.data(32)
        createProject.updateProject(project_path)

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

    def getFocusedProject(self):
        item = self.projectList_lwd.currentItem()
        return item

    def archiveProject(self, item):
        if not item:
            return None
        old_path = item.data(32)
        project_name = os.path.split(old_path)[-1]
        archive_folder = settings.SettingsClass().load()['archive']
        new_path = os.path.join(archive_folder, project_name)
        if os.path.exists(new_path):
            message = QMessageBox()
            message.setWindowTitle('Cannot Move to Archive')
            message.setText('There is a project named "{0}" in the archive.\nPlease, rename the project and try again.'.format(project_name))
            message.exec_()
        else:
            shutil.move(old_path, new_path)
        self.update_list()

    def backupProject(self, item):
        if not item:
            return None
        old_path = item.data(32)
        project_name = os.path.split(old_path)[-1]
        current_time = time.strftime('%Y-%m-%d_%H-%M-%S')
        backup_folder = settings.SettingsClass().load()['backup']
        new_path = os.path.join(backup_folder, project_name, current_time)
        zipfolder.zipFolder(old_path, new_path)
        self.update_list()

    def openFolder(self, folder):
        try:
            path = settings.SettingsClass().load()[folder]
            if not os.path.exists(path):
                os.mkdir(path)
            webbrowser.open(path)
        except KeyError:
            pass


if __name__ == '__main__':
    app = QApplication([])
    w = ProjectManagerClass()
    w.show()
    app.exec_()
