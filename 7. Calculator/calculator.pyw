#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtGui import *
from decimal import *
import calculator_UIs as ui


class Calculator(QMainWindow, ui.Ui_Calculator):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setupUi(self)

        # Attributes
        self.__value = '455.66'
        self.__value_sign = False
        self.__display_value_sign = self.get_display_value_sign()
        self.__previous_value = '776'
        self.__next_operation = 'addition'
        self.__display_next_operation = self.get_display_next_operation()

        self.__display_all()

        # Key press actions
        self.ce_btn.clicked.connect(self.clear_value)
        self.c_btn.clicked.connect(self.clear_all)
        self.sign_reversal_btn.clicked.connect(self.change_sign)
        self.division_btn.clicked.connect(lambda: self.choose_next_operation('division'))
        self.multiplication_btn.clicked.connect(lambda: self.choose_next_operation('multiplication'))
        self.subtraction_btn.clicked.connect(lambda: self.choose_next_operation('subtraction'))
        self.addition_btn.clicked.connect(lambda: self.choose_next_operation('addition'))
        self.calculate_btn.clicked.connect(self.calculate_expression)
        self.backspace_btn.clicked.connect(self.remove_last_symbol)
        self.digit0_btn.clicked.connect(lambda: self.add_digit('0'))
        self.digit1_btn.clicked.connect(lambda: self.add_digit('1'))
        self.digit2_btn.clicked.connect(lambda: self.add_digit('2'))
        self.digit3_btn.clicked.connect(lambda: self.add_digit('3'))
        self.digit4_btn.clicked.connect(lambda: self.add_digit('4'))
        self.digit5_btn.clicked.connect(lambda: self.add_digit('5'))
        self.digit6_btn.clicked.connect(lambda: self.add_digit('6'))
        self.digit7_btn.clicked.connect(lambda: self.add_digit('7'))
        self.digit8_btn.clicked.connect(lambda: self.add_digit('8'))
        self.digit9_btn.clicked.connect(lambda: self.add_digit('9'))
        self.decimal_mark_btn.clicked.connect(self.add_decimal_delimiter)

    def __display_all(self):
        """Mapping attributes to UI labels"""
        self.__display_value_sign = self.get_display_value_sign()
        self.__display_next_operation = self.get_display_next_operation()
        self.value_lb.setText(self.__value)
        self.value_sign_lb.setText(self.__display_value_sign)
        self.previous_value_lb.setText(self.__previous_value)
        self.next_operation_lb.setText(self.__display_next_operation)

    def get_display_value_sign(self):
        if self.__value_sign:
            return ''
        else:
            return '-'

    def get_display_next_operation(self):
        no = self.__next_operation
        if no == 'division':
            return '÷'
        elif no == 'multiplication':
            return '×'
        elif no == 'subtraction':
            return '-'
        elif no == 'addition':
            return '+'
        else:
            return ''

    def clear_all(self):
        self.__value = '0'
        self.__value_sign = True
        self.__previous_value = ''
        self.__next_operation = ''
        self.__display_all()

    def clear_value(self):
        self.__value = '0'
        self.__value_sign = True
        self.__display_all()

    def add_digit(self, digit):
        if digit in '0123456789':
            self.__value = self.__value + digit
        self.__display_all()

    def add_decimal_delimiter(self):
        if '.' not in self.__value:
            self.__value = self.__value + '.'
        self.__display_all()

    def remove_last_symbol(self):
        """Remove last digit or decimal delimiter"""
        self.__value = self.__value[:-1]
        if not self.__value:
            self.__value = '0'
        self.__display_all()

    def change_sign(self):
        self.__value_sign = not self.__value_sign
        self.__display_all()

    def choose_next_operation(self, operation):
        if operation in ['division', 'multiplication',
                         'subtraction', 'addition']:
            self.__next_operation = operation
        self.__display_all()

    def calculate_expression(self):
        no = self.__next_operation
        v = Decimal(self.__display_value_sign + self.__value)
        pv = Decimal(self.__previous_value)

        if no == 'division':
            v = pv / v
        elif no == 'multiplication':
            v = pv * v
        elif no == 'subtraction':
            v = pv - v
        elif no == 'addition':
            v = pv + v

        if v < 0:
            self.__value_sign = False
            self.__value = str(abs(v))
        else:
            self.__value_sign = True
            self.__value = str(v)

        self.__previous_value = ''
        self.__next_operation = ''
        self.__display_all()


if __name__ == '__main__':
    app = QApplication([])
    w = Calculator()
    w.show()
    app.exec_()
