#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtGui import *
from widgets import createProject_UI as ui


class CreateProjectDialogClass(QDialog, ui.Ui_createDialog):
    def __init__(self, parent):
        super(CreateProjectDialogClass, self).__init__(parent)
        self.setupUi(self)
        # connects
        self.create_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)


