from PySide.QtCore import *
from PySide.QtGui import *


class splineRampWidget(QWidget):
    def __init__(self):
        super(splineRampWidget, self).__init__()
        self.resize(500, 300)

        self.lineWidth = 3
        self.pointSize = 30

        self.point1 = QPoint(0, 10)
        self.point2 = QPoint(500, 250)


    def paintEvent(self, event):
        rec = event.rect()  # When displayed area changed
        if False:   # For autocomplete in PyCharm
            rec = QRect()
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(rec, Qt.black)

        path = QPainterPath()
        path.moveTo(self.point1)
        path.cubicTo(rec.width()/2, self.point1.y(),
                     rec.width()/2, self.point2.y(),
                     rec.width(), self.point2.y())
        painter.setPen(QPen(QBrush(Qt.white), 3))
        painter.drawPath(path)

        painter.setBrush(QBrush(Qt.white))
        painter.drawEllipse(self.point1, self.pointSize, self.pointSize)
        painter.drawEllipse(self.point2, self.pointSize, self.pointSize)

        painter.end()


if __name__ == '__main__':
    app = QApplication([])
    w = splineRampWidget()
    w.show()
    app.exec_()
