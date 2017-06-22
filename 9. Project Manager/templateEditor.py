#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PySide.QtGui import *
from PySide.QtCore import *
from widgets import templateEditor_UI as ui
import os, json


templateFile = os.path.join(os.path.dirname(__file__), 'template.json')


class TemplateEditorClass(QWidget, ui.Ui_templateEditor):
    def __init__(self):
        super(TemplateEditorClass, self).__init__()
        self.setupUi(self)

        #ui
        self.tree.setDragDropMode(QAbstractItemView.InternalMove)
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # connects
        self.add_btn.clicked.connect(self.addItem)
        self.remove_btn.clicked.connect(self.removeItem)
        self.save_btn.clicked.connect(self.saveTemplate)
        self.close_btn.clicked.connect(self.close)

        # start
        self.loadTemplate()

    def addItem(self, name='Folder', parent=None):
        name = self.sanitizeItemName(name)
        if not parent:
            parent = self.tree.invisibleRootItem()
        item = QTreeWidgetItem()
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable |
                      Qt.ItemIsEditable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
        item.setText(0, name)
        parent.addChild(item)
        item.setExpanded(1)
        return item

    def removeItem(self):
        items = self.tree.selectedItems()
        for i in items:
            i_index = self.tree.indexFromItem(i).row()
            (i.parent() or self.tree.invisibleRootItem()).takeChild(i_index)

    def saveTemplate(self):
        template = self.getStructure()
        with open(templateFile, 'w') as f:
            json.dump(template, f, indent=4)
        self.close()

    def getStructure(self, parent=None):
        level = []
        if not parent:
            parent = self.tree.invisibleRootItem()
        for i in range(parent.childCount()):
            ch = parent.child(i)
            content = self.getStructure(ch)
            level.append({'name': ch.text(0),
                          'content': content})
        return level

    def loadTemplate(self):
        if os.path.exists(templateFile):
            with open(templateFile) as f:
                template = json.load(f)
                self.restoreStructure(template)

    def restoreStructure(self, data, parent=None):
        if not parent:
            parent = self.tree.invisibleRootItem()
        for i in data:
            item = self.addItem(i['name'], parent)
            self.restoreStructure(i['content'], item)

    def sanitizeItemName(self, name, parent=None):
        'Names must be unique on the same level and not operating system reserved words'
        name = self.removeForbiddenSymbols(name)
        if not name:
            name = 'Folder'
        if not parent:
            parent = self.tree.invisibleRootItem()
        child_names = []
        for child_index in range(parent.childCount()):
            item = parent.child(child_index)
            child_names.append(item.text(0))
        forbidden_names = ['CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5',
                           'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5',
                           'LPT6', 'LPT7', 'LPT8', 'LPT9']
        forbidden_names = forbidden_names + child_names
        if name not in forbidden_names:
            return name
        else:
            new_name = name
            index = 1
            while new_name in forbidden_names:
                new_name = name + ' (' + str(index) + ')'
                index += 1
            return new_name

    @staticmethod
    def removeForbiddenSymbols(name):
        'Letters, numbers and some other symbols allowed'
        name = name.strip()
        allowed_symbols = '()_- '
        correct_name = []
        for char in name:
            if char.isalpha() or char.isdigit() or char in allowed_symbols:
                correct_name.append(char)
        correct_name = ''.join(correct_name)
        return correct_name
