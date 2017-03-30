#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtGui import *
import calculator_UIs as ui


class Calculator(QMainWindow, ui.Ui_Calculator):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setupUi(self)

        self.__value = 0
        self.__value_sign = True
        self.__previous_value = None
        self.__next_operation = None


    def clear_all(self):
        pass

    def clear_value(self):
        pass

    def add_digit(self, digit):
        pass

    def remove_last_symbol(self):
        """Remove last digit or decimal delimiter"""
        pass

    def add_decimal_delimiter(self):
        pass

    def change_sign(self):
        pass

    def choose_next_operation(self, operation):
        pass

    def calculate_expression(self):
        pass





if __name__ == '__main__':
    app = QApplication([])
    w = Calculator()
    w.show()
    app.exec_()

