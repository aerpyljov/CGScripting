from PySide.QtCore import *
from PySide.QtGui import *


class pickerClass(QWidget):

    colorChangedSignal = Signal(QColor)

    def __init__(self):
        super(pickerClass, self).__init__()
        self.sz = 500
        self.setFixedSize(QSize(self.sz, self.sz))
        self.img = self.getRamp()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rec = event.rect()
        painter.drawImage(0, 0, self.img)
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
        self.getColor(event.pos())

    def getColor(self, pos):
        h = pos.x() / float(self.sz)
        s = pos.y() / float(self.sz)
        c = QColor()
        c.setHsvF(h, s, 1)
        self.colorChangedSignal.emit(c)

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
        self.picker.colorChangedSignal.connect(self.updateColor)

    def updateColor(self, color):
        palette = self.color.palette()
        palette.setColor(self.color.backgroundRole(), color)
        self.color.setPalette(palette)



if __name__ == '__main__':
    app = QApplication([])
    w = colorPickerWindow()
    w.show()
    app.exec_()
