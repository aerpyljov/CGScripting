# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexey\Documents\GitHub\CGScripting\9. Project Manager\widgets\createProject.ui'
#
# Created: Thu Aug 24 19:59:55 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_createDialog(object):
    def setupUi(self, createDialog):
        createDialog.setObjectName("createDialog")
        createDialog.resize(403, 300)
        self.verticalLayout = QtGui.QVBoxLayout(createDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.name_lb = QtGui.QLabel(createDialog)
        self.name_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_lb.setObjectName("name_lb")
        self.gridLayout.addWidget(self.name_lb, 0, 0, 1, 1)
        self.name_le = QtGui.QLineEdit(createDialog)
        self.name_le.setObjectName("name_le")
        self.gridLayout.addWidget(self.name_le, 0, 1, 1, 1)
        self.comment_lb = QtGui.QLabel(createDialog)
        self.comment_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.comment_lb.setObjectName("comment_lb")
        self.gridLayout.addWidget(self.comment_lb, 1, 0, 1, 1)
        self.comment_pte = QtGui.QPlainTextEdit(createDialog)
        self.comment_pte.setObjectName("comment_pte")
        self.gridLayout.addWidget(self.comment_pte, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create_btn = QtGui.QPushButton(createDialog)
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout.addWidget(self.create_btn)
        self.cancel_btn = QtGui.QPushButton(createDialog)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(createDialog)
        QtCore.QMetaObject.connectSlotsByName(createDialog)

    def retranslateUi(self, createDialog):
        createDialog.setWindowTitle(QtGui.QApplication.translate("createDialog", "Create Project", None, QtGui.QApplication.UnicodeUTF8))
        self.name_lb.setText(QtGui.QApplication.translate("createDialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.comment_lb.setText(QtGui.QApplication.translate("createDialog", "Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.create_btn.setText(QtGui.QApplication.translate("createDialog", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("createDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

