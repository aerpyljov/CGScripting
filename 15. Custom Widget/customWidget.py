from PySide.QtCore import *
from PySide.QtGui import *

class drawCustomWidget(QWidget):
    def __init__(self):
        super(drawCustomWidget, self).__init__()
        self.resize(300, 200)
        self.setWindowTitle('Custom Widget')


if __name__ == '__main__':
    app = QApplication([])
    w = drawCustomWidget()
    w.show()
    app.exec_()