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
        self.browseImagemagick_btn.clicked.connect(self.select_exe)
        self.browseOut_btn.clicked.connect(self.select_destination_folder)
        self.clearOut_btn.clicked.connect(self.clear_destination_folder)

    def start(self):
        files = self.list.getAllFiles()
        if files:
            out = self.out_le.text()
            inc = 100 / len(files)
            for f in files:
                converter.convert(f, out)
                self.progressBar.setValue(self.progressBar.value() + inc)
        self.progressBar.setValue(0)


    def select_exe(self):
        dialog = QFileDialog()
        filename, used_filter = dialog.getOpenFileName(caption="Select magick.exe file",
                                filter="magick.exe", option=dialog.DontUseNativeDialog)
        if filename:
            self.imagemagick_lb.setText(filename)
        #TODO: save to settings


    def select_destination_folder(self):
        dialog = QFileDialog()
        chosen_folder = self.out_le.text()
        if chosen_folder:
            dialog.setDirectory(chosen_folder)
        foldername = dialog.getExistingDirectory(caption="Select destination folder")
        if foldername:
            self.out_le.setText(foldername)
        #TODO: save to settings


    def clear_destination_folder(self):
        self.out_le.setText('')
        # TODO: save to settings

if __name__ == '__main__':
    app = QApplication([])
    w = ImageConverterClass()
    w.show()
    app.exec_()