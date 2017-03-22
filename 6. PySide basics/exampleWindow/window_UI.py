# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\exampleWindow\window.ui'
#
# Created: Fri Sep 19 13:07:43 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_example(object):
    def setupUi(self, example):
        example.setObjectName(_fromUtf8("example"))
        example.resize(241, 204)
        self.verticalLayout_2 = QtGui.QVBoxLayout(example)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.additem_btn = QtGui.QPushButton(example)
        self.additem_btn.setObjectName(_fromUtf8("additem_btn"))
        self.verticalLayout_2.addWidget(self.additem_btn)
        self.name_le = QtGui.QLineEdit(example)
        self.name_le.setObjectName(_fromUtf8("name_le"))
        self.verticalLayout_2.addWidget(self.name_le)
        self.items_ly = QtGui.QVBoxLayout()
        self.items_ly.setObjectName(_fromUtf8("items_ly"))
        self.verticalLayout_2.addLayout(self.items_ly)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(example)
        QtCore.QMetaObject.connectSlotsByName(example)

    def retranslateUi(self, example):
        example.setWindowTitle(_translate("example", "Item List", None))
        self.additem_btn.setText(_translate("example", "Add", None))

