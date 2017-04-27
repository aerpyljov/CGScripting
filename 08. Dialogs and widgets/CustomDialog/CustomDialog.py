from PySide.QtGui import *
import dialog

class simpleWindow(QWidget):
    def __init__(self):
        super(simpleWindow, self).__init__()
        ly = QVBoxLayout(self)
        self.btn  = QPushButton('Open')
        ly.addWidget(self.btn)
        self.resize(300,200)
        self.btn.clicked.connect(self.showMessage)

    def showMessage(self):
        self.dial = dialog.dialogClass()
        r = self.dial.exec_()
        if r:
            print self.dial.getData()

if __name__ == '__main__':
    app = QApplication([])
    w = simpleWindow()
    w.show()
    app.exec_()
    