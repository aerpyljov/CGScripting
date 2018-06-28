from PySide.QtCore import *
from PySide.QtGui import *


class splineRampWidget(QWidget):
    def __init__(self):
        super(splineRampWidget, self).__init__()
        self.resize(500, 300)

        self.lineWidth = 3
        self.pointSize = 10

        self.point1 = QPointF(0, 10)
        self.point2 = QPointF(100, 10)
        self.point3 = QPointF(500, 250)
        self.dragged = None  # Either point1 or point2 to be moved

        self.factor1 = 0.0
        self.factor2x = 0.5
        self.factor2y = 0.5
        self.factor3 = 1.0

        self.region1 = QRect()
        self.region2 = QRect()
        self.region3 = QRect()
        self.regionSize = 40
        self.updateRegions()

    def updateRegions(self):
        self.region1 = QRect(0, 0, self.regionSize, self.regionSize)
        self.region1.moveCenter(self.point1.toPoint())  # Works with QPoint, not QPointF
        self.region2 = QRect(0, 0, self.regionSize, self.regionSize)
        self.region2.moveCenter(self.point2.toPoint())
        self.region3 = QRect(0, 0, self.regionSize, self.regionSize)
        self.region3.moveCenter(self.point3.toPoint())

        self.factor1 = self.point1.y() / float(self.size().height())
        self.factor2x = self.point2.x() / float(self.size().width())
        self.factor2y = self.point2.y() / float(self.size().height())
        self.factor3 = self.point3.y() / float(self.size().height())


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
        path.cubicTo(rec.width() / 2, self.point1.y(),
                     self.point2.x(), self.point2.y(),
                     rec.width(), self.point3.y())
        painter.setPen(QPen(QBrush(Qt.white), 3))
        painter.drawPath(path)

        painter.setBrush(QBrush(Qt.white))
        painter.drawEllipse(self.point1, self.pointSize, self.pointSize)
        painter.drawEllipse(self.point2, self.pointSize, self.pointSize)
        painter.drawEllipse(self.point3, self.pointSize, self.pointSize)

        # Paint the regions for drag'n'drop
        # painter.setPen(QPen(QBrush(Qt.white), 1))
        # painter.setBrush(Qt.NoBrush)
        # painter.drawRect(self.region1)
        # painter.drawRect(self.region2)
        # painter.drawRect(self.region3)

        painter.end()

    def mousePressEvent(self, event):
        if (self.region1.contains(event.pos())):
            self.dragged = self.point1
        elif (self.region2.contains(event.pos())):
            self.dragged = self.point2
        elif (self.region3.contains(event.pos())):
            self.dragged = self.point3
        super(splineRampWidget, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if not self.dragged is None:  # Zero is a valid value
            y = event.pos().y()
            x = event.pos().x()
            s = self.size()
            self.dragged.setY(min(max(y, 1), s.height()))  # Prevent moving outside the widget
            if self.dragged == self.point2:
                self.dragged.setX(min(max(x, 1), s.width()))
            self.update()
        super(splineRampWidget, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.dragged = None
        self.updateRegions()
        self.update()
        super(splineRampWidget, self).mouseReleaseEvent(event)

    def resizeEvent(self, event):
        self.point1.setY(event.size().height() * self.factor1)
        self.point2.setY(event.size().height() * self.factor2y)
        self.point2.setX(event.size().width() * self.factor2x)
        self.point3.setY(event.size().height() * self.factor3)
        self.point3.setX(event.size().width())
        self.updateRegions()
        self.update()
        super(splineRampWidget, self).resizeEvent(event)



if __name__ == '__main__':
    app = QApplication([])
    w = splineRampWidget()
    w.show()
    app.exec_()
