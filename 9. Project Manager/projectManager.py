#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import os, webbrowser, shutil, time
from PySide.QtCore import *
from PySide.QtGui import *
from widgets import projectManager_UI as ui, projectListWidget
from icons import resources
import settingsDialog, createProjectDialog, templateEditor, settings, createProject, zipfolder


class ProjectManagerClass(QMainWindow, ui.Ui_projectManager):
    def __init__(self):
        super(ProjectManagerClass, self).__init__()
        self.setupUi(self)

        # widgets
        self.projectList_lwd = projectListWidget.ProjectListClass()
        self.projectList_ly.addWidget(self.projectList_lwd)

        # ui
        self.projectList_lwd.setDragDropMode(QAbstractItemView.DragDrop)
        self.projectList_lwd.setDefaultDropAction(Qt.MoveAction)
        self.projectList_lwd.setContextMenuPolicy(Qt.CustomContextMenu)
        self.setWindowIcon(QIcon(':/ico32/appicon.png'))
        self.create_btn.setIcon(QIcon(':/ico32/createproject.png'))
        self.update_btn.setIcon(QIcon(':/ico32/updateproject.png'))
        self.backup_btn.setIcon(QIcon(':/ico32/movebackup.png'))
        self.archive_btn.setIcon(QIcon(':/ico32/movearchive.png'))
        self.openBackup_btn.setIcon(QIcon(':/ico32/openfolder.png'))
        self.openBackup_btn.setText('')
        self.openArchive_btn.setIcon(QIcon(':/ico32/openfolder.png'))
        self.openArchive_btn.setText('')
        self.refresh_btn.setIcon(QIcon(':/ico32/refresh.png'))
        self.settings_btn.setIcon(QIcon(':/ico32/setting.png'))
        self.templateEditor_btn.setIcon(QIcon(':/ico32/templateeditor.png'))

        # connects
        self.projectList_lwd.customContextMenuRequested.connect(self.openProjectMenu)
        self.projectList_lwd.drop_notifier.itemDropped.connect(self.dropEvent)
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
            item = self.projectList_lwd.item(0)
            self.projectList_lwd.setCurrentItem(item)

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

    def openProjectMenu(self, pos):
        pos = self.sender().mapToGlobal(pos)
        menu = QMenu()
        # Prepare actions for the menu
        act_create_project = QAction('Create Project', self,
                                     triggered=self.create_project)
        act_update_project = QAction('Update Project', self,
                                     triggered=(lambda: self.update_project(self.getFocusedProject())))
        act_backup = QAction('Move to BACKUP', self,
                             triggered=(lambda: self.backupProject(self.getFocusedProject())))
        act_archive = QAction('Move to ARCHIVE', self,
                             triggered=(lambda: self.archiveProject(self.getFocusedProject())))
        act_refresh = QAction('Refresh', self, triggered=self.update_list)
        # Fill the menu
        menu.addAction(act_create_project)
        if self.getFocusedProject():
            menu.addSeparator()
            menu.addAction(act_update_project)
            menu.addAction(act_backup)
            menu.addAction(act_archive)
        menu.addSeparator()
        menu.addAction(act_refresh)
        menu.exec_(pos)

    def dropEvent(self, event):  # TODO: intercept drop event
        print('HELP')
        self.update_list()


if __name__ == '__main__':
    app = QApplication([])
    w = ProjectManagerClass()
    w.show()
    app.exec_()
