# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexey\Documents\GitHub\CGScripting\9. Project Manager\widgets\templateEditor.ui'
#
# Created: Thu May 11 19:25:50 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_templateEditor(object):
    def setupUi(self, templateEditor):
        templateEditor.setObjectName("templateEditor")
        templateEditor.resize(595, 568)
        self.verticalLayout = QtGui.QVBoxLayout(templateEditor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_btn = QtGui.QPushButton(templateEditor)
        self.add_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.add_btn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout_2.addWidget(self.add_btn)
        self.remove_btn = QtGui.QPushButton(templateEditor)
        self.remove_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.remove_btn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.remove_btn.setFont(font)
        self.remove_btn.setObjectName("remove_btn")
        self.horizontalLayout_2.addWidget(self.remove_btn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tree = QtGui.QTreeWidget(templateEditor)
        self.tree.setObjectName("tree")
        self.tree.headerItem().setText(0, "1")
        self.tree.header().setVisible(False)
        self.verticalLayout.addWidget(self.tree)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_btn = QtGui.QPushButton(templateEditor)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout.addWidget(self.save_btn)
        self.close_btn = QtGui.QPushButton(templateEditor)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(templateEditor)
        QtCore.QMetaObject.connectSlotsByName(templateEditor)

    def retranslateUi(self, templateEditor):
        templateEditor.setWindowTitle(QtGui.QApplication.translate("templateEditor", "Template Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.add_btn.setText(QtGui.QApplication.translate("templateEditor", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_btn.setText(QtGui.QApplication.translate("templateEditor", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.save_btn.setText(QtGui.QApplication.translate("templateEditor", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.close_btn.setText(QtGui.QApplication.translate("templateEditor", "Close", None, QtGui.QApplication.UnicodeUTF8))

