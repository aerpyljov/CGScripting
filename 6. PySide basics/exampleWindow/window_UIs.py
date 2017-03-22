# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\exampleWindow\window.ui'
#
# Created: Fri Sep 19 13:07:43 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_example(object):
    def setupUi(self, example):
        example.setObjectName("example")
        example.resize(241, 204)
        self.verticalLayout_2 = QtGui.QVBoxLayout(example)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.additem_btn = QtGui.QPushButton(example)
        self.additem_btn.setObjectName("additem_btn")
        self.verticalLayout_2.addWidget(self.additem_btn)
        self.name_le = QtGui.QLineEdit(example)
        self.name_le.setObjectName("name_le")
        self.verticalLayout_2.addWidget(self.name_le)
        self.items_ly = QtGui.QVBoxLayout()
        self.items_ly.setObjectName("items_ly")
        self.verticalLayout_2.addLayout(self.items_ly)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(example)
        QtCore.QMetaObject.connectSlotsByName(example)

    def retranslateUi(self, example):
        example.setWindowTitle(QtGui.QApplication.translate("example", "Item List", None, QtGui.QApplication.UnicodeUTF8))
        self.additem_btn.setText(QtGui.QApplication.translate("example", "Add", None, QtGui.QApplication.UnicodeUTF8))

