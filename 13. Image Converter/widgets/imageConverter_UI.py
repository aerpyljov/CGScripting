# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexey\Documents\GitHub\CGScripting\13. Image Cînverter\imageConverter.ui'
#
# Created: Thu Dec 14 20:07:33 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_imageConverter(object):
    def setupUi(self, imageConverter):
        imageConverter.setObjectName("imageConverter")
        imageConverter.resize(800, 600)
        self.centralwidget = QtGui.QWidget(imageConverter)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imagemagick_lb = QtGui.QLabel(self.centralwidget)
        self.imagemagick_lb.setObjectName("imagemagick_lb")
        self.horizontalLayout.addWidget(self.imagemagick_lb)
        self.browseImagemagick_btn = QtGui.QPushButton(self.centralwidget)
        self.browseImagemagick_btn.setMinimumSize(QtCore.QSize(30, 0))
        self.browseImagemagick_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.browseImagemagick_btn.setObjectName("browseImagemagick_btn")
        self.horizontalLayout.addWidget(self.browseImagemagick_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.files_ly = QtGui.QVBoxLayout()
        self.files_ly.setObjectName("files_ly")
        self.verticalLayout.addLayout(self.files_ly)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.out_le = QtGui.QLineEdit(self.centralwidget)
        self.out_le.setObjectName("out_le")
        self.horizontalLayout_2.addWidget(self.out_le)
        self.browseOut_btn = QtGui.QPushButton(self.centralwidget)
        self.browseOut_btn.setMinimumSize(QtCore.QSize(30, 0))
        self.browseOut_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.browseOut_btn.setObjectName("browseOut_btn")
        self.horizontalLayout_2.addWidget(self.browseOut_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.start_btn = QtGui.QPushButton(self.centralwidget)
        self.start_btn.setObjectName("start_btn")
        self.verticalLayout.addWidget(self.start_btn)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout.setStretch(1, 1)
        imageConverter.setCentralWidget(self.centralwidget)

        self.retranslateUi(imageConverter)
        QtCore.QMetaObject.connectSlotsByName(imageConverter)

    def retranslateUi(self, imageConverter):
        imageConverter.setWindowTitle(QtGui.QApplication.translate("imageConverter", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.imagemagick_lb.setText(QtGui.QApplication.translate("imageConverter", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.browseImagemagick_btn.setText(QtGui.QApplication.translate("imageConverter", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.browseOut_btn.setText(QtGui.QApplication.translate("imageConverter", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.start_btn.setText(QtGui.QApplication.translate("imageConverter", "Start", None, QtGui.QApplication.UnicodeUTF8))

