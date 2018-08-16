from PySide.QtCore import *
from PySide.QtGui import *


class pickerClass(QWidget):
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



if __name__ == '__main__':
    app = QApplication([])
    w = pickerClass()
    w.show()
    app.exec_()
