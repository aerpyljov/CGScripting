from PySide.QtCore import *
from PySide.QtGui import *
from math import sin


class sineWidget(QWidget):
    def __init__(self):
        super(sineWidget, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('Sine')

        self.wave_height = 30
        self.wave_len = 20

    def paintEvent(self, event):
        rec = event.rect()  # When displayed area changed
        if False:   # For autocomplete in PyCharm
            rec = QRect()
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(rec, Qt.black)
        painter.setPen(QPen(QBrush(Qt.white), 1))
        prev_x = 0
        prev_y = 0
        for x in range(1, rec.width()):
            s = sin(x*0.1)
            y = (s * self.wave_height) + (rec.height()/2)
            painter.drawLine(QPointF(prev_x, prev_y),
                             QPointF(x, y))
            prev_x = x
            prev_y = y
        painter.end()


if __name__ == '__main__':
    app = QApplication([])
    w = sineWidget()
    w.show()
    app.exec_()
