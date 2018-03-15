#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtGui import *
from widgets import imageConverter_UI as ui, filesWidget
import os
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
        self.browseOut_btn.clicked.connect(self.select_destination_folder)
        self.clearOut_btn.clicked.connect(self.clear_destination_folder)
        self.addFolder_btn.clicked.connect(self.add_folder)
        self.addImage_btn.clicked.connect(self.add_image)
        self.remove_btn.clicked.connect(self.remove)
        self.showPaths_btn.clicked.connect(self.show_paths)

        # connects for saving settings
        self.subfolders_chb.stateChanged.connect(lambda: self.save_settings(
                                                     'IncludeSubfoldersFlag',
                                                     self.subfolders_chb.isChecked()))
        self.skip_rbtn.toggled.connect(lambda: self.save_settings(
                                        'NameCollisionResolutionPolicy', 'Skip')
                                        if self.skip_rbtn.isChecked() else
                                        self.save_settings(
                                        'NameCollisionResolutionPolicy', 'Replace'))
        self.formatOut_cbox.currentIndexChanged.connect(lambda:
                                        self.save_settings('DestinationFormat',
                                        self.formatOut_cbox.currentText()))

        # start
        self.stop_btn.hide()  # Cannot work while conversion is done in the UI thread
        self.browseImagemagick_btn.hide() # Changed the app - magick.exe has fixed location
        self.initialize()

    def initialize(self):
        defaults = settings.SettingsClass().load()
        #
        app_folder = os.path.dirname(os.path.abspath(__file__))
        imageMagickPath = os.path.join(app_folder, 'ImageMagick', 'magick.exe')
        self.imagemagick_lb.setText(imageMagickPath)
        #
        includeSubfoldersFlag = defaults.get('IncludeSubfoldersFlag')
        if includeSubfoldersFlag:
            self.subfolders_chb.setChecked(True)
        else:
            self.subfolders_chb.setChecked(False)
        #
        destinationFolder = defaults.get('DestinationFolder')
        if destinationFolder:
            self.out_le.setText(destinationFolder)
        #
        nameCollisionResolutionPolicy = defaults.get('NameCollisionResolutionPolicy')
        if nameCollisionResolutionPolicy == 'Skip':
            self.skip_rbtn.setChecked(True)
        else:
            self.replace_rbtn.setChecked(True)
        #
        destinationFormat = defaults.get('DestinationFormat')
        supportedFormats = []
        for item in range(0, self.formatOut_cbox.count()):
            fileformat = self.formatOut_cbox.itemText(item)
            supportedFormats.append(fileformat)
        if destinationFormat in supportedFormats:
            index = self.formatOut_cbox.findText(destinationFormat)
            self.formatOut_cbox.setCurrentIndex(index)

    def save_settings(self, key, value):
        data = settings.SettingsClass().load()
        data[key] = value
        settings.SettingsClass().save(data)

    def start(self):
        include_subfolders = self.subfolders_chb.isChecked()
        files = self.list.getImagesFromFolders(include_subfolders)
        if files:
            trg_ext = self.formatOut_cbox.currentText().lower()
            out = self.out_le.text()
            overwrite = True if self.replace_rbtn.isChecked() else False
            inc = 100 / len(files)
            for f in files:
                converter.convert(f, trg_ext, out, overwrite)
                self.progressBar.setValue(self.progressBar.value() + inc)
        self.progressBar.setValue(0)

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

    def add_folder(self):
        dialog = QFileDialog()
        foldername = dialog.getExistingDirectory(caption="Select folder with images")
        if foldername:
            self.list.addFile(foldername)

    def add_image(self):
        dialog = QFileDialog()
        imagenames, used_filter = dialog.getOpenFileNames(caption="Select images")
        if imagenames:
            for image in imagenames:
                self.list.addFile(image)

    def remove(self):
        self.list.deleteSelected()

    def show_paths(self):
        for i in range(self.list.count()):
            item = self.list.item(i)
            fullpath = item.data(32)  # QtCore.Qt.ItemDataRole = Qt.UserRole
            name = os.path.basename(fullpath)
            if self.showPaths_btn.isChecked():
                item.setText(fullpath)
            else:
                item.setText(name)


if __name__ == '__main__':
    app = QApplication([])
    w = ImageConverterClass()
    w.show()
    app.exec_()