#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtGui import *
from widgets import settingsDialog_UI as ui


class SettingsDialogClass(QDialog, ui.Ui_settingsDialog):
    def __init__(self, parent):
        super(SettingsDialogClass, self).__init__(parent)
        self.setupUi(self)

