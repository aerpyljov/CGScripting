#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PySide.QtGui import *
from PySide.QtCore import *


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        layout = QVBoxLayout(self)

        main_label = QLabel('Enter any words and push the button:')
        layout.addWidget(main_label)

        line = QLineEdit()
        layout.addWidget(line)
        line.textChanged.connect(self.text)

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
        print 'ACTION'

    def text(self, arg):
        print arg

app = QApplication([])
window = MyWidget()
window.show()
app.exec_()
