from PySide.QtGui import *

class myWidget(QWidget):
    def __init__(self):
        super(myWidget, self).__init__()
        l = QVBoxLayout()
        self.setLayout(l)
        label = QLabel('Text')
        l.addWidget(label)
        b = QPushButton('OK')
        l.addWidget(b)

app = QApplication([])
w = myWidget()
w.show()
app.exec_()