from PySide.QtGui import *

app = QApplication([])
w = QWidget()
l = QHBoxLayout()
w.setLayout(l)
label = QLabel('Text')
l.addWidget(label)
b = QPushButton('OK')
l.addWidget(b)
w.show()
app.exec_()