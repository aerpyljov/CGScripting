#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
from PySide.QtGui import *


class MyWidget(QWidget):
    """
    A widget with a static main label, a field for typing a line of text, a button
    and the second label, that displays the text user entered after the button is pushed.
    """
    def __init__(self, caption):
        super(MyWidget, self).__init__()
        self.setWindowTitle(caption)

        self.__text = ''

        self.layout = QVBoxLayout(self)

        main_label = QLabel('Enter any words and push the button:')
        self.layout.addWidget(main_label)

        self.line = QLineEdit()
        self.layout.addWidget(self.line)
        self.line.textChanged.connect(self.set_text)

        self.button = QPushButton('Print')
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.display_text)    # First way to work with signals and slots

        self.result_label = QLabel()
        self.layout.addWidget(self.result_label)

        """
        # Second way to work with signals and slots
        self.connect(self.button, SIGNAL('clicked()'),
                     self, SLOT('action()'))

        # Third way to work with signals and slots
        @self.button.clicked.connect
        def click():
            self.action()
        """

    def display_text(self):
        self.result_label.setText(self.__text)

    def set_text(self, arg):
        self.__text = arg

app = QApplication([])

window = MyWidget('Simple widget')
window.show()

app.exec_()
