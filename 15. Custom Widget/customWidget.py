from PySide.QtCore import *
from PySide.QtGui import *

class drawCustomWidget(QWidget):
    def __init__(self):
        super(drawCustomWidget, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('Custom Widget')

    def paintEvent(self, event):
        rec = event.rect()  # When displayed area changed
        if False:   # For autocomplete in PyCharm
            rec = QRect()
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Make lines smooth
        painter.fillRect(rec, Qt.black)  # Background

        painter.setPen(QPen(QBrush(Qt.red), 3))
        painter.setBrush(QBrush(Qt.black))  # Filling
        painter.drawRect(30, 30, rec.width()-60, rec.height()-60)  # 60, because left and top margins are 30, and we need to compensate them

        painter.setPen(QPen(QBrush(Qt.green), 8))  # Color and size of the line
        painter.drawLine(0, 0, rec.width(), rec.height())

        painter.end()


if __name__ == '__main__':
    app = QApplication([])
    w = drawCustomWidget()
    w.show()
    app.exec_()
