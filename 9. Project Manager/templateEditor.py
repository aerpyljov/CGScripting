#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtGui import *
from widgets import templateEditor_UI as ui


class TemplateEditorClass(QDialog, ui.Ui_templateEditor):
    def __init__(self):
        super(TemplateEditorClass, self).__init__()
        self.setupUi(self)
        # connects

