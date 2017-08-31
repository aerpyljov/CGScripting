#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtGui import *
from PySide import QtCore
from widgets import settingsDialog_UI as ui
import settings


class SettingsDialogClass(QDialog, ui.Ui_settingsDialog):
    def __init__(self, parent):
        super(SettingsDialogClass, self).__init__(parent)
        self.setupUi(self)

        # ui
        self.table.setColumnCount(2)
        self.table.horizontalHeader().setStretchLastSection(1)
        self.setWindowIcon(QIcon(':/ico32/setting.png'))
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        
        # start
        self.fill_table()

    def fill_table(self):
        data = settings.SettingsClass().load()
        for key, value in data.items():
            self.add_parm(key, value)

    def add_parm(self, parm, value):
        row_number = self.table.rowCount()  # The last number
        self.table.insertRow(row_number)

        item = QTableWidgetItem()
        item.setText(parm)
        self.table.setItem(row_number, 0, item)

        item = QTableWidgetItem()
        item.setText(value)
        self.table.setItem(row_number, 1, item)

    def get_table_data(self):
        data = dict()
        for i in range(self.table.rowCount()):
            parm = self.table.item(i, 0).text()
            value = self.table.item(i, 1).text()
            data[parm] = value
        return data