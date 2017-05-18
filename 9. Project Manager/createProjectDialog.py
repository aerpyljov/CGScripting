#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtGui import *
from widgets import createProject_UI as ui


class CreateProjectDialogClass(QDialog, ui.Ui_createDialog):
    def __init__(self, parent):
        super(CreateProjectDialogClass, self).__init__(parent)
        self.setupUi(self)
        # connects
        self.create_btn.clicked.connect(self.doCreate)
        self.cancel_btn.clicked.connect(self.reject)

    def doCreate(self):
        if self.name_le.text():
            self.accept()

    def getDialogData(self):
        return dict(
            name = self.name_le.text(),
            comment = self.comment_pte.toPlainText()
        )
