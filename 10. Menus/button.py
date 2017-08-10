from PySide.QtCore import *
from PySide.QtGui import *
textArray = 'Click', 'Press', 'Enter'

class myButton(QPushButton):
    def __init__(self, text):
        super(myButton, self).__init__(text)
        # self.btn.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.btn.customContextMenuRequested.connect(self.openMenu)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            super(myButton, self).mousePressEvent(event)
        elif event.button() == Qt.MouseButton.RightButton:
            pos = event.globalPos()
            menu = QMenu()
            for i in textArray:
                menu.addAction( QAction(i, self) )
            a = menu.exec_(pos)
            if a:
                self.setText(a.text())
        elif event.button() == Qt.MouseButton.MiddleButton:
            pass