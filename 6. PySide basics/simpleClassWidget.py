#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PySide.QtGui import *


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()    # Obligatory
        layout = QVBoxLayout()
        self.setLayout(layout)
        label = QLabel('Эта кнопка тоже ничего не делает:')
        layout.addWidget(label)
        button = QPushButton('Проверить')
        layout.addWidget(button)


app = QApplication([])
w = MyWidget()
w.show()
app.exec_()
