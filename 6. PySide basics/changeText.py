from PySide.QtCore import *
from PySide.QtGui import *

class simpleWindowClass(QWidget):
    def __init__(self):
        super(simpleWindowClass, self).__init__()
        layout = QVBoxLayout(self)
        self.label = QLabel('Text')
        layout.addWidget(self.label)
        self.button = QPushButton('Press')
        layout.addWidget(self.button)
        self.button.clicked.connect(self.action)

    def action(self):
        self.label.setText('New Text')
        self.button.setText('Presseed')
        self.button.clicked.connect(self.close)

if __name__ == '__main__':
    app = QApplication([])
    w = simpleWindowClass()
    w.show()
    app.exec_()
