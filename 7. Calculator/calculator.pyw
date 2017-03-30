#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function, division
from PySide.QtGui import *
from decimal import *
import calculator_UIs as ui


class Calculator(QMainWindow, ui.Ui_Calculator):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setupUi(self)

        self.__value = Decimal('0')
        self.__value_sign = True
        self.__previous_value = None
        self.__next_operation = None

    def clear_all(self):
        self.__value = Decimal('0')
        self.__value_sign = True
        self.__previous_value = None
        self.__next_operation = None

    def clear_value(self):
        self.__value = Decimal('0')
        self.__value_sign = True

    def add_digit(self, digit):
        pass

    def remove_last_symbol(self):
        """Remove last digit or decimal delimiter"""
        pass

    def add_decimal_delimiter(self):
        pass

    def change_sign(self):
        self.__value_sign = not self.__value_sign

    def choose_next_operation(self, operation):
        if operation in ['division', 'multiplication',
                         'subtraction', 'addition']:
            self.__next_operation = operation

    def calculate_expression(self):
        if self.__next_operation == 'division':
            self.__value = self.__previous_value / self.__value
        elif self.__next_operation == 'multiplication':
            self.__value = self.__previous_value * self.__value
        elif self.__next_operation == 'subtraction':
            self.__value = self.__previous_value - self.__value
        elif self.__next_operation == 'addition':
            self.__value = self.__previous_value + self.__value



if __name__ == '__main__':
    app = QApplication([])
    w = Calculator()
    w.show()
    app.exec_()

