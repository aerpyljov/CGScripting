from PySide.QtCore import *
from PySide.QtGui import *
from math import sin
import sineWidget_UI as ui


class sineWidget(QWidget):
    def __init__(self):
        super(sineWidget, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('Sine')

        self.wave_height = 30
        self.wave_len = 20
        self.pen_width = 3
        self.grid = 30

    def paintEvent(self, event):
        rec = event.rect()  # When displayed area changed
        if False:   # For autocomplete in PyCharm
            rec = QRect()
        painter = QPainter()
        painter.begin(self)
        # paint
        painter.fillRect(rec, Qt.black)
        painter.setPen(QPen(QBrush(Qt.gray), 0.5))
        for i in range(0, rec.width(), self.grid):
            painter.drawLine(i, 0, i, rec.height())
        for i in range(0, rec.height(), self.grid):
            painter.drawLine(0, i, rec.width(), i)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(QBrush(Qt.yellow), self.pen_width))
        prev_x = 0
        prev_y = (0 * self.wave_height) + (rec.height()/2)
        for x in range(1, rec.width()):
            s = sin(x*0.1*self.wave_len*0.1)
            y = (s * self.wave_height) + (rec.height()/2)
            painter.drawLine(QPointF(prev_x, prev_y),
                             QPointF(x, y))
            prev_x = x
            prev_y = y
        painter.end()

    def setHeight(self, height):
        self.wave_height = height
        self.update()

    def setLen(self, len):
        self.wave_len = len
        self.update()

    def setWidth(self, width):
        self.pen_width = width
        self.update()

    def setGrid(self, grid):
        self.grid = grid
        self.update()

class SineWindowClass(QMainWindow, ui.Ui_SineWidgetWindow):
    def __init__(self):
        super(SineWindowClass, self).__init__()
        self.setupUi(self)
        self.sine = sineWidget()
        self.sine_ly.addWidget(self.sine)
        self.heigth_hs.setValue(20)
        self.length_hs.setValue(20)
        self.width_hs.setValue(1)
        # connects
        self.heigth_hs.valueChanged.connect(self.sine.setHeight)
        self.length_hs.valueChanged.connect(self.sine.setLen)
        self.width_hs.valueChanged.connect(self.sine.setWidth)
        self.grid_hs.valueChanged.connect(self.sine.setGrid)


if __name__ == '__main__':
    app = QApplication([])
    w = SineWindowClass()
    w.show()
    app.exec_()
