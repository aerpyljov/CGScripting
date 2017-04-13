#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PySide.QtGui import *
from decimal import *
import calculator_UIs as ui


class Calculator(QMainWindow, ui.Ui_Calculator):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setupUi(self)

        # Attributes
        self.__value = '0'
        self.__value_sign = True
        self.__previous_value = '0'
        self.__last_used_value = None
        self.__next_operation = ''
        self.__last_used_operation = None
        self.__just_calculated = False
        self.__error_division_by_zero = False
        self.__display_value = self.__get_display_value()
        self.__display_value_sign = self.__get_display_value_sign()
        self.__display_next_operation = self.__get_display_next_operation()

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
        self.__display_value = self.__get_display_value()
        self.__display_value_sign = self.__get_display_value_sign()
        self.__display_next_operation = self.__get_display_next_operation()
        self.value_lb.setText(self.__display_value)
        self.value_sign_lb.setText(self.__display_value_sign)
        self.previous_value_lb.setText(self.__previous_value if (self.__previous_value != '0' or self.__display_next_operation) else None)
        self.next_operation_lb.setText(self.__display_next_operation)

    def __get_display_value(self):
        if self.__just_calculated:
            if self.__error_division_by_zero:
                return 'Cannot divide by zero'
            else:
                return self.__previous_value[:25] # To fit the app width
        else:
            return self.__value[:25] # To fit the app width

    def __get_display_value_sign(self):
        if self.__value_sign:
            return ''
        else:
            return '-'

    def __get_display_next_operation(self):
        no = self.__next_operation
        if no == 'division':
            return '÷'
        elif no == 'multiplication':
            return '×'
        elif no == 'subtraction':
            return '-'
        elif no == 'addition':
            return '+'

    def clear_value(self):
        self.__value = '0'
        self.__value_sign = True
        self.__last_used_value = None
        self.__last_used_operation = None
        self.__just_calculated = False
        self.__error_division_by_zero = False
        self.__display_all()

    def clear_all(self):
        self.__previous_value = '0'
        self.__next_operation = ''
        self.clear_value()

    def add_digit(self, digit):
        if digit in '0123456789':
            if self.__value == '0':
                self.__value = digit
            else:
                self.__value = self.__value + digit
        self.__just_calculated = False
        self.__error_division_by_zero = False
        self.__display_all()

    def add_decimal_delimiter(self):
        if '.' not in self.__value:
            self.__value = self.__value + '.'
            self.__just_calculated = False
        self.__just_calculated = False
        self.__error_division_by_zero = False
        self.__display_all()

    def remove_last_symbol(self):
        """Remove last digit or decimal delimiter"""
        self.__value = self.__value[:-1]
        if not self.__value:
            self.__value = '0'
            self.__value_sign = True
        self.__just_calculated = False
        self.__error_division_by_zero = False
        self.__display_all()

    def change_sign(self):
        if self.__value == '0':
            self.__value_sign = True
        else:
            self.__value_sign = not self.__value_sign
        self.__just_calculated = False
        self.__error_division_by_zero = False
        self.__display_all()

    def choose_next_operation(self, operation):
        if not self.__just_calculated and self.__value != '0':
            self.calculate_expression()
        if operation in ['division', 'multiplication','subtraction', 'addition']:
            self.__next_operation = operation
        self.__just_calculated = False
        self.__error_division_by_zero = False
        self.__display_all()

    def calculate_expression(self):
        pv = Decimal(self.__previous_value)

        # If '=' pressed again, repeat the last operation
        if self.__just_calculated:
            v = self.__last_used_value
            operation = self.__last_used_operation
        else:
            v = Decimal(self.__display_value_sign + self.__value)
            operation = self.__next_operation
            self.__last_used_value = v
            self.__last_used_operation = operation

        if pv == Decimal('0'):
            operation = ''

        if operation == 'division':
            if v == Decimal('0'):
                self.__error_division_by_zero = True
            else:
                v = pv / v
        elif operation == 'multiplication':
            v = pv * v
        elif operation == 'subtraction':
            v = pv - v
        elif operation == 'addition':
            v = pv + v

        self.__value_sign = True
        self.__value = '0'

        self.__previous_value = str(v)
        self.__just_calculated = True
        self.__display_all()


if __name__ == '__main__':
    app = QApplication([])
    w = Calculator()
    w.show()
    app.exec_()

