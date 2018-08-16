from PySide.QtCore import *
from PySide.QtGui import *


class pickerClass(QWidget):
    def __init__(self):
        super(pickerClass, self).__init__()
        self.resize(300, 300)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rec = event.rect()
        color = QColor()
        for x in range(rec.width()):
            h = x / float(rec.width())
            for y in range(rec.height()):
                s = y / float(rec.height())
                v = 1
                color.setHsvF(h, s, v)
                painter.setPen(QPen(QBrush(color), 1))
                painter.drawPoint(x, y)

        painter.end()


if __name__ == '__main__':
    app = QApplication([])
    w = pickerClass()
    w.show()
    app.exec_()
