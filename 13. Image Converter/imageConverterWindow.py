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
        self.addFolder_btn.setIcon(QIcon(':/ico32/addfolder.png'))
        self.addImage_btn.setIcon(QIcon(':/ico32/addimage.png'))
        self.remove_btn.setIcon(QIcon(':/ico32/remove.png'))
        self.showPaths_btn.setIcon(QIcon(':/ico32/showhidepaths.png'))
        self.start_btn.setIcon(QIcon(':/ico32/start.png'))

        # connects
        self.start_btn.clicked.connect(self.start)
        self.browseImagemagick_btn.clicked.connect(self.select_exe)
        self.browseOut_btn.clicked.connect(self.select_destination_folder)
        self.clearOut_btn.clicked.connect(self.clear_destination_folder)

        # connects for saving settings
        self.subfolders_chb.stateChanged.connect(lambda: self.save_settings(
                                                     'IncludeSubfoldersFlag',
                                                     self.subfolders_chb.isChecked()))
        self.skip_rbtn.toggled.connect(lambda: self.save_settings(
                                        'NameCollisionResolutionPolicy', 'Skip')
                                        if self.skip_rbtn.isChecked() else
                                        self.save_settings(
                                        'NameCollisionResolutionPolicy', 'Replace'))

        # start
        self.initialize()

    def initialize(self):
        defaults = settings.SettingsClass().load()
        imageMagickPath = defaults.get('ImageMagickPath')
        if imageMagickPath:
            self.imagemagick_lb.setText(imageMagickPath)
        includeSubfoldersFlag = defaults.get('IncludeSubfoldersFlag')
        if includeSubfoldersFlag:
            self.subfolders_chb.setChecked(True)
        else:
            self.subfolders_chb.setChecked(False)
        destinationFolder = defaults.get('DestinationFolder')
        if destinationFolder:
            self.out_le.setText(destinationFolder)
        nameCollisionResolutionPolicy = defaults.get('NameCollisionResolutionPolicy')
        if nameCollisionResolutionPolicy == 'Skip':
            self.skip_rbtn.setChecked(True)
        else:
            self.replace_rbtn.setChecked(True)

    def save_settings(self, key, value):
        data = settings.SettingsClass().load()
        data[key] = value
        settings.SettingsClass().save(data)

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
            self.save_settings('ImageMagickPath', filename)


    def select_destination_folder(self):
        dialog = QFileDialog()
        chosen_folder = self.out_le.text()
        if chosen_folder:
            dialog.setDirectory(chosen_folder)
        foldername = dialog.getExistingDirectory(caption="Select destination folder")
        if foldername:
            self.out_le.setText(foldername)
            self.save_settings('DestinationFolder', foldername)


    def clear_destination_folder(self):
        self.out_le.setText('')
        self.save_settings('DestinationFolder', None)

if __name__ == '__main__':
    app = QApplication([])
    w = ImageConverterClass()
    w.show()
    app.exec_()