# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexey\Documents\GitHub\CGScripting\15. Custom Widget\sineWidget\sineWidget.ui'
#
# Created: Thu Apr 12 20:01:02 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SineWidgetWindow(object):
    def setupUi(self, SineWidgetWindow):
        SineWidgetWindow.setObjectName("SineWidgetWindow")
        SineWidgetWindow.resize(850, 694)
        self.centralwidget = QtGui.QWidget(SineWidgetWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.width_lb = QtGui.QLabel(self.centralwidget)
        self.width_lb.setObjectName("width_lb")
        self.gridLayout.addWidget(self.width_lb, 2, 0, 1, 1)
        self.heigth_lb = QtGui.QLabel(self.centralwidget)
        self.heigth_lb.setObjectName("heigth_lb")
        self.gridLayout.addWidget(self.heigth_lb, 1, 0, 1, 1)
        self.length_hs = QtGui.QSlider(self.centralwidget)
        self.length_hs.setMinimum(1)
        self.length_hs.setMaximum(50)
        self.length_hs.setOrientation(QtCore.Qt.Horizontal)
        self.length_hs.setObjectName("length_hs")
        self.gridLayout.addWidget(self.length_hs, 0, 2, 1, 1)
        self.grid_lb = QtGui.QLabel(self.centralwidget)
        self.grid_lb.setObjectName("grid_lb")
        self.gridLayout.addWidget(self.grid_lb, 3, 0, 1, 1)
        self.length_lb = QtGui.QLabel(self.centralwidget)
        self.length_lb.setObjectName("length_lb")
        self.gridLayout.addWidget(self.length_lb, 0, 0, 1, 1)
        self.grid_hs = QtGui.QSlider(self.centralwidget)
        self.grid_hs.setMinimum(10)
        self.grid_hs.setMaximum(100)
        self.grid_hs.setOrientation(QtCore.Qt.Horizontal)
        self.grid_hs.setObjectName("grid_hs")
        self.gridLayout.addWidget(self.grid_hs, 3, 2, 1, 1)
        self.heigth_hs = QtGui.QSlider(self.centralwidget)
        self.heigth_hs.setMinimum(1)
        self.heigth_hs.setMaximum(200)
        self.heigth_hs.setOrientation(QtCore.Qt.Horizontal)
        self.heigth_hs.setObjectName("heigth_hs")
        self.gridLayout.addWidget(self.heigth_hs, 1, 2, 1, 1)
        self.width_hs = QtGui.QSlider(self.centralwidget)
        self.width_hs.setMinimum(1)
        self.width_hs.setMaximum(20)
        self.width_hs.setOrientation(QtCore.Qt.Horizontal)
        self.width_hs.setObjectName("width_hs")
        self.gridLayout.addWidget(self.width_hs, 2, 2, 1, 1)
        self.grid_num_lb = QtGui.QLabel(self.centralwidget)
        self.grid_num_lb.setObjectName("grid_num_lb")
        self.gridLayout.addWidget(self.grid_num_lb, 3, 3, 1, 1)
        self.width_num_lb = QtGui.QLabel(self.centralwidget)
        self.width_num_lb.setObjectName("width_num_lb")
        self.gridLayout.addWidget(self.width_num_lb, 2, 3, 1, 1)
        self.heigth_num_lb = QtGui.QLabel(self.centralwidget)
        self.heigth_num_lb.setObjectName("heigth_num_lb")
        self.gridLayout.addWidget(self.heigth_num_lb, 1, 3, 1, 1)
        self.length_num_lb = QtGui.QLabel(self.centralwidget)
        self.length_num_lb.setObjectName("length_num_lb")
        self.gridLayout.addWidget(self.length_num_lb, 0, 3, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.sine_ly = QtGui.QVBoxLayout()
        self.sine_ly.setObjectName("sine_ly")
        self.verticalLayout_3.addLayout(self.sine_ly)
        SineWidgetWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SineWidgetWindow)
        QtCore.QMetaObject.connectSlotsByName(SineWidgetWindow)

    def retranslateUi(self, SineWidgetWindow):
        SineWidgetWindow.setWindowTitle(QtGui.QApplication.translate("SineWidgetWindow", "Sine Widget", None, QtGui.QApplication.UnicodeUTF8))
        self.width_lb.setText(QtGui.QApplication.translate("SineWidgetWindow", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.heigth_lb.setText(QtGui.QApplication.translate("SineWidgetWindow", "Heigth", None, QtGui.QApplication.UnicodeUTF8))
        self.grid_lb.setText(QtGui.QApplication.translate("SineWidgetWindow", "Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.length_lb.setText(QtGui.QApplication.translate("SineWidgetWindow", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.grid_num_lb.setText(QtGui.QApplication.translate("SineWidgetWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.width_num_lb.setText(QtGui.QApplication.translate("SineWidgetWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.heigth_num_lb.setText(QtGui.QApplication.translate("SineWidgetWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.length_num_lb.setText(QtGui.QApplication.translate("SineWidgetWindow", "0", None, QtGui.QApplication.UnicodeUTF8))

