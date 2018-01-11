#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtGui import *
from widgets import imageConverter_UI as ui, filesWidget
import converter, settings
from icons import resources


class ImageConverterClass(QMainWindow, ui.Ui_imageConverter):
    def __init__(self):
        super(ImageConverterClass, self).__init__()
        self.setupUi(self)

        # widgets
        self.list = filesWidget.listWidgetClass()
        self.files_ly.addWidget(self.list)

        # icons
        self.setWindowIcon(QIcon(':/ico32/appicon.png'))

        # connects
        self.start_btn.clicked.connect(self.start)

    def start(self):
        files = self.list.getAllFiles()
        if files:
            out = self.out_le.text()
            inc = 100 / len(files)
            for f in files:
                converter.convert(f, out)
                self.progressBar.setValue(self.progressBar.value() + inc)
        self.progressBar.setValue(0)


if __name__ == '__main__':
    app = QApplication([])
    w = ImageConverterClass()
    w.show()
    app.exec_()