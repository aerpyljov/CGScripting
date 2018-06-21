from PySide.QtCore import *
from PySide.QtGui import *


class splineRampWidget(QWidget):
    def __init__(self):
        super(splineRampWidget, self).__init__()
        self.resize(500, 300)

        self.lineWidth = 3
        self.pointSize = 10

        self.point1 = QPoint(0, 10)
        self.point2 = QPoint(500, 250)
        self.dragged = None  # Either point1 or point2 to be moved

        self.region1 = QRect()
        self.region2 = QRect()
        self.regionSize = 40
        self.updateRegions()

    def updateRegions(self):
        self.region1 = QRect(0, 0, self.regionSize, self.regionSize)
        self.region1.moveCenter(self.point1)
        self.region2 = QRect(0, 0, self.regionSize, self.regionSize)
        self.region2.moveCenter(self.point2)


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

        painter.setPen(QPen(QBrush(Qt.white), 1))
        painter.setBrush(Qt.NoBrush)
        painter.drawRect(self.region1)
        painter.drawRect(self.region2)
        painter.end()

    def mousePressEvent(self, event):
        if (self.region1.contains(event.pos())):
            self.dragged = self.point1
        elif (self.region2.contains(event.pos())):
            self.dragged = self.point2
        super(splineRampWidget, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.dragged:
            self.dragged.setY(event.pos().y())
            self.update()
        super(splineRampWidget, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.dragged = None
        self.updateRegions()
        self.update()
        super(splineRampWidget, self).mouseReleaseEvent(event)


if __name__ == '__main__':
    app = QApplication([])
    w = splineRampWidget()
    w.show()
    app.exec_()
