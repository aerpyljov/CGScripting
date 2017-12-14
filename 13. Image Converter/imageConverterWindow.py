#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
from widgets import imageConverter_UI as ui, filesWidget

class ImageConverterClass(QMainWindow, ui.Ui_imageConverter):
    def __init__(self):
        super(ImageConverterClass, self).__init__()
        self.setupUi(self)
        self.list = filesWidget.listWidgetClass()
        self.files_ly.addWidget(self.list)


if __name__ == '__main__':
    app = QApplication([])
    w = ImageConverterClass()
    w.show()
    app.exec_()