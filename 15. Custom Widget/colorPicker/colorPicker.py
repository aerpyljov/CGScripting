from PySide.QtCore import *
from PySide.QtGui import *


class pickerClass(QWidget):

    colorChangedSignal = Signal(QColor)

    def __init__(self):
        super(pickerClass, self).__init__()
        self.sz = 500
        self.setFixedSize(QSize(self.sz, self.sz))
        self.img = self.getRamp()
        self.markerSize = 6
        self.markerPos = None
        self.preview = None
        self.setAttribute(Qt.WA_Hover)
        self.installEventFilter(self)
        self.setCursor(Qt.BlankCursor)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rec = event.rect()
        painter.drawImage(0, 0, self.img)
        if self.markerPos:
            painter.setPen(QPen(QBrush(Qt.black), 3))
            painter.drawEllipse(self.markerPos, self.markerSize, self.markerSize)
        if self.preview:
            painter.setPen(QPen(QBrush(QColor(0, 0, 0, 50)), 3))
            painter.drawEllipse(self.preview, self.markerSize, self.markerSize)
        painter.end()

    def getRamp(self):
        img = QImage(self.sz, self.sz, QImage.Format_RGB32)
        color = QColor()
        for x in range(self.sz):
            h = x / float(self.sz)
            for y in range(self.sz):
                s = y / float(self.sz)
                v = 1
                color.setHsvF(h, s, v)
                img.setPixel(x, y, color.rgb())
        return img

    def mousePressEvent(self, event):
        super(pickerClass, self).mousePressEvent(event)
        self.markerPos = event.pos()
        self.getColor(event.pos())
        self.update()

    def mouseMoveEvent(self, event):
        super(pickerClass, self).mouseMoveEvent(event)
        self.markerPos = event.pos()
        self.getColor(event.pos())
        self.update()

    def getColor(self, pos):
        h = pos.x() / float(self.sz)
        s = pos.y() / float(self.sz)
        c = QColor()
        c.setHsvF(h, s, 1)
        self.colorChangedSignal.emit(c)

    def eventFilter(self, obj, event):  # There is no mouseHoverEvent in QWidget
        if event.type() == QEvent.HoverMove:
            self.preview = event.pos()
            self.update()
            return True
        if event.type() == QEvent.HoverLeave:
            self.preview = None
            self.update()
            return True
        return False


class colorPickerWindow(QWidget):
    def __init__(self):
        super(colorPickerWindow, self).__init__()
        self.ly = QVBoxLayout(self)
        self.color = QLabel()
        self.color.setAutoFillBackground(True)
        self.color.setMinimumHeight(40)
        self.ly.addWidget(self.color)
        self.picker = pickerClass()
        self.ly.addWidget(self.picker)
        self.colorCode = QLabel()
        self.colorCode.setMinimumHeight(40)
        self.ly.addWidget(self.colorCode)
        self.picker.colorChangedSignal.connect(self.updateColor)

    def updateColor(self, color):
        palette = self.color.palette()
        palette.setColor(self.color.backgroundRole(), color)
        self.color.setPalette(palette)
        rgbCode = color.getRgb()
        rgbCode = str(rgbCode[:3])
        self.colorCode.setText('RGB: ' + rgbCode)



if __name__ == '__main__':
    app = QApplication([])
    w = colorPickerWindow()
    w.show()
    app.exec_()
