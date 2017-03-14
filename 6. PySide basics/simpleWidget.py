#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PySide.QtGui import *


"Create an application"
app = QApplication([])

"Create a widget - an empty window"
widget = QWidget()

"All labels, buttons, etc. must be put on a layout"
layout = QHBoxLayout()  # Horizontal layout
widget.setLayout(layout)

label = QLabel('Кнопка ничего не делает:')
layout.addWidget(label)
button = QPushButton('Проверить')
layout.addWidget(button)

"Make the widget visible"
widget.show()

"Run the application"
app.exec_()
