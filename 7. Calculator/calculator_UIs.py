# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexey\Documents\GitHub\CGScripting\7. Calculator\calculator.ui'
#
# Created: Thu Apr 13 19:38:45 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.setEnabled(True)
        Calculator.resize(600, 350)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Calculator.sizePolicy().hasHeightForWidth())
        Calculator.setSizePolicy(sizePolicy)
        Calculator.setMinimumSize(QtCore.QSize(600, 350))
        Calculator.setMaximumSize(QtCore.QSize(600, 350))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        Calculator.setFont(font)
        self.centralwidget = QtGui.QWidget(Calculator)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.previous_value_lb = QtGui.QLabel(self.centralwidget)
        self.previous_value_lb.setText("")
        self.previous_value_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.previous_value_lb.setObjectName("previous_value_lb")
        self.horizontalLayout.addWidget(self.previous_value_lb)
        self.next_operation_lb = QtGui.QLabel(self.centralwidget)
        self.next_operation_lb.setText("")
        self.next_operation_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.next_operation_lb.setObjectName("next_operation_lb")
        self.horizontalLayout.addWidget(self.next_operation_lb)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.value_sign_lb = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.value_sign_lb.setFont(font)
        self.value_sign_lb.setText("")
        self.value_sign_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.value_sign_lb.setObjectName("value_sign_lb")
        self.horizontalLayout_2.addWidget(self.value_sign_lb)
        self.value_lb = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.value_lb.setFont(font)
        self.value_lb.setText("")
        self.value_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.value_lb.setObjectName("value_lb")
        self.horizontalLayout_2.addWidget(self.value_lb)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ce_btn = QtGui.QPushButton(self.centralwidget)
        self.ce_btn.setObjectName("ce_btn")
        self.gridLayout.addWidget(self.ce_btn, 3, 0, 1, 1)
        self.c_btn = QtGui.QPushButton(self.centralwidget)
        self.c_btn.setObjectName("c_btn")
        self.gridLayout.addWidget(self.c_btn, 3, 1, 1, 1)
        self.backspace_btn = QtGui.QPushButton(self.centralwidget)
        self.backspace_btn.setObjectName("backspace_btn")
        self.gridLayout.addWidget(self.backspace_btn, 3, 2, 1, 1)
        self.division_btn = QtGui.QPushButton(self.centralwidget)
        self.division_btn.setObjectName("division_btn")
        self.gridLayout.addWidget(self.division_btn, 3, 3, 1, 1)
        self.digit9_btn = QtGui.QPushButton(self.centralwidget)
        self.digit9_btn.setObjectName("digit9_btn")
        self.gridLayout.addWidget(self.digit9_btn, 4, 2, 1, 1)
        self.digit8_btn = QtGui.QPushButton(self.centralwidget)
        self.digit8_btn.setObjectName("digit8_btn")
        self.gridLayout.addWidget(self.digit8_btn, 4, 1, 1, 1)
        self.calculate_btn = QtGui.QPushButton(self.centralwidget)
        self.calculate_btn.setFlat(False)
        self.calculate_btn.setObjectName("calculate_btn")
        self.gridLayout.addWidget(self.calculate_btn, 7, 3, 1, 1)
        self.digit6_btn = QtGui.QPushButton(self.centralwidget)
        self.digit6_btn.setObjectName("digit6_btn")
        self.gridLayout.addWidget(self.digit6_btn, 5, 2, 1, 1)
        self.subtraction_btn = QtGui.QPushButton(self.centralwidget)
        self.subtraction_btn.setObjectName("subtraction_btn")
        self.gridLayout.addWidget(self.subtraction_btn, 5, 3, 1, 1)
        self.digit0_btn = QtGui.QPushButton(self.centralwidget)
        self.digit0_btn.setObjectName("digit0_btn")
        self.gridLayout.addWidget(self.digit0_btn, 7, 1, 1, 1)
        self.digit7_btn = QtGui.QPushButton(self.centralwidget)
        self.digit7_btn.setObjectName("digit7_btn")
        self.gridLayout.addWidget(self.digit7_btn, 4, 0, 1, 1)
        self.multiplication_btn = QtGui.QPushButton(self.centralwidget)
        self.multiplication_btn.setObjectName("multiplication_btn")
        self.gridLayout.addWidget(self.multiplication_btn, 4, 3, 1, 1)
        self.digit4_btn = QtGui.QPushButton(self.centralwidget)
        self.digit4_btn.setObjectName("digit4_btn")
        self.gridLayout.addWidget(self.digit4_btn, 5, 0, 1, 1)
        self.digit2_btn = QtGui.QPushButton(self.centralwidget)
        self.digit2_btn.setObjectName("digit2_btn")
        self.gridLayout.addWidget(self.digit2_btn, 6, 1, 1, 1)
        self.digit1_btn = QtGui.QPushButton(self.centralwidget)
        self.digit1_btn.setObjectName("digit1_btn")
        self.gridLayout.addWidget(self.digit1_btn, 6, 0, 1, 1)
        self.sign_reversal_btn = QtGui.QPushButton(self.centralwidget)
        self.sign_reversal_btn.setObjectName("sign_reversal_btn")
        self.gridLayout.addWidget(self.sign_reversal_btn, 7, 0, 1, 1)
        self.decimal_mark_btn = QtGui.QPushButton(self.centralwidget)
        self.decimal_mark_btn.setObjectName("decimal_mark_btn")
        self.gridLayout.addWidget(self.decimal_mark_btn, 7, 2, 1, 1)
        self.addition_btn = QtGui.QPushButton(self.centralwidget)
        self.addition_btn.setObjectName("addition_btn")
        self.gridLayout.addWidget(self.addition_btn, 6, 3, 1, 1)
        self.digit3_btn = QtGui.QPushButton(self.centralwidget)
        self.digit3_btn.setObjectName("digit3_btn")
        self.gridLayout.addWidget(self.digit3_btn, 6, 2, 1, 1)
        self.digit5_btn = QtGui.QPushButton(self.centralwidget)
        self.digit5_btn.setObjectName("digit5_btn")
        self.gridLayout.addWidget(self.digit5_btn, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        Calculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QtGui.QApplication.translate("Calculator", "Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.ce_btn.setText(QtGui.QApplication.translate("Calculator", "CE", None, QtGui.QApplication.UnicodeUTF8))
        self.c_btn.setText(QtGui.QApplication.translate("Calculator", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.backspace_btn.setText(QtGui.QApplication.translate("Calculator", "←", None, QtGui.QApplication.UnicodeUTF8))
        self.division_btn.setText(QtGui.QApplication.translate("Calculator", "÷", None, QtGui.QApplication.UnicodeUTF8))
        self.digit9_btn.setText(QtGui.QApplication.translate("Calculator", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.digit8_btn.setText(QtGui.QApplication.translate("Calculator", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.calculate_btn.setText(QtGui.QApplication.translate("Calculator", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.digit6_btn.setText(QtGui.QApplication.translate("Calculator", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.subtraction_btn.setText(QtGui.QApplication.translate("Calculator", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.digit0_btn.setText(QtGui.QApplication.translate("Calculator", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.digit7_btn.setText(QtGui.QApplication.translate("Calculator", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.multiplication_btn.setText(QtGui.QApplication.translate("Calculator", "×", None, QtGui.QApplication.UnicodeUTF8))
        self.digit4_btn.setText(QtGui.QApplication.translate("Calculator", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.digit2_btn.setText(QtGui.QApplication.translate("Calculator", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.digit1_btn.setText(QtGui.QApplication.translate("Calculator", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.sign_reversal_btn.setText(QtGui.QApplication.translate("Calculator", "±", None, QtGui.QApplication.UnicodeUTF8))
        self.decimal_mark_btn.setText(QtGui.QApplication.translate("Calculator", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.addition_btn.setText(QtGui.QApplication.translate("Calculator", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.digit3_btn.setText(QtGui.QApplication.translate("Calculator", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.digit5_btn.setText(QtGui.QApplication.translate("Calculator", "5", None, QtGui.QApplication.UnicodeUTF8))

