from PySide.QtCore import *
from PySide.QtGui import *

textArray = 'Click', 'Press', 'Enter'

class widgetMenuClass(QWidget):
    def __init__(self):
        super(widgetMenuClass, self).__init__()
        ly = QVBoxLayout(self)
        self.btn = QPushButton('Click')
        ly.addWidget(self.btn)
        self.line = QLineEdit()
        ly.addWidget(self.line)
        
        self.btn.setContextMenuPolicy(Qt.CustomContextMenu)
        self.btn.customContextMenuRequested.connect(self.openMenu)
        
        self.line.setContextMenuPolicy(Qt.CustomContextMenu)
        self.line.customContextMenuRequested.connect(self.openMenu)

    def openMenu(self, pos):
        pos = self.sender().mapToGlobal(pos)
        try:
            menu = self.sender().createStandardContextMenu()
        except:
            menu = QMenu()
        for i in textArray:
            menu.addAction( QAction(i, self) )
        a = menu.exec_(pos)
        if a:
            self.sender().setText(a.text())



if __name__ == '__main__':
    app = QApplication([])
    w = widgetMenuClass()
    w.show()
    app.exec_()