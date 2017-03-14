from PySide.QtGui import *
from PySide.QtCore import *

class myWidget(QWidget):
    def __init__(self):
        super(myWidget, self).__init__()
        layout = QVBoxLayout(self)
        button = QPushButton('Print')
        layout.addWidget(button)
        button.clicked.connect(self.action)
        line =QLineEdit()
        layout.addWidget(line)
        line.textChanged.connect(self.text)
        # self.connect(button, SIGNAL('clicked()'),
        #              self, SLOT('action()'))
        @button.clicked.connect
        def click():
            self.action()

    def action(self):
        print 'ACTION'

    def text(self, arg):
        print arg

app = QApplication([])
window = myWidget()
window.show()
app.exec_()
