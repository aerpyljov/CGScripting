#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
from PySide.QtGui import *
from PySide.QtCore import *


class MyWidget(QWidget):
    """
    A widget with a static main label, a field for typing a line of text, a button
    and the second label, that displays the text user entered after the button is pushed.
    """
    def __init__(self):
        super(MyWidget, self).__init__()

        self.text = ''

        layout = QVBoxLayout(self)

        main_label = QLabel('Enter any words and push the button:')
        layout.addWidget(main_label)

        line = QLineEdit()
        layout.addWidget(line)
        line.textChanged.connect(self.set_text)

        button = QPushButton('Print')
        layout.addWidget(button)

        button.clicked.connect(self.action)    # First way to work with signals and slots

        result_label = QLabel()
        layout.addWidget(result_label)

        """
        # Second way to work with signals and slots
        self.connect(button, SIGNAL('clicked()'),
                     self, SLOT('action()'))

        # Third way to work with signals and slots
        @button.clicked.connect
        def click():
            self.action()
        """

    def action(self):
        print(self.text)

    def set_text(self, arg):
        self.text = arg

app = QApplication([])
window = MyWidget()
window.show()
app.exec_()
