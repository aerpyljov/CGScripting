from PySide.QtCore import *
from PySide.QtGui import *
from math import sin
import sineWidget_UI as ui


class sineWidget(QWidget):
    def __init__(self, wave_height, wave_len, pen_width, grid):
        super(sineWidget, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('Sine')

        self.wave_height = wave_height
        self.wave_len = wave_len
        self.pen_width = pen_width
        self.grid = grid

    def paintEvent(self, event):
        rec = event.rect()  # When displayed area changed
        if False:   # For autocomplete in PyCharm
            rec = QRect()
        painter = QPainter()
        painter.begin(self)
        # paint
        painter.fillRect(rec, Qt.black)
        painter.setPen(QPen(QBrush(Qt.gray), 0.5))
        painter.setFont(QFont('Arial', 8))
        for i in range(0, rec.width(), self.grid):
            painter.drawLine(i, 0, i, rec.height())
            if self.grid >= 30:
                painter.drawText(i+3, 12, str(i))
        for i in range(0, rec.height(), self.grid):
            painter.drawLine(0, i, rec.width(), i)
        painter.setPen(QPen(QBrush(Qt.gray), 3))
        painter.drawLine(0, rec.height()/2, rec.width(), rec.height()/2)
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
        self.heigth_hs.setValue(100)
        self.length_hs.setValue(5)
        self.width_hs.setValue(1)
        self.grid_hs.setValue(50)
        self.sine = sineWidget(self.heigth_hs.value(), self.length_hs.value(),
                               self.width_hs.value(), self.grid_hs.value())
        self.sine_ly.addWidget(self.sine)
        #
        self.heigth_num_lb.setText(str(self.heigth_hs.value()))
        self.length_num_lb.setText(str(self.length_hs.value()))
        self.width_num_lb.setText(str(self.width_hs.value()))
        self.grid_num_lb.setText(str(self.grid_hs.value()))
        # connects
        self.heigth_hs.valueChanged.connect(self.sine.setHeight)
        self.length_hs.valueChanged.connect(self.sine.setLen)
        self.width_hs.valueChanged.connect(self.sine.setWidth)
        self.grid_hs.valueChanged.connect(self.sine.setGrid)
        #
        self.heigth_hs.valueChanged.connect(lambda x: self.heigth_num_lb.setText(str(x)))
        self.length_hs.valueChanged.connect(lambda x: self.length_num_lb.setText(str(x)))
        self.width_hs.valueChanged.connect(lambda x: self.width_num_lb.setText(str(x)))
        self.grid_hs.valueChanged.connect(lambda x: self.grid_num_lb.setText(str(x)))

if __name__ == '__main__':
    app = QApplication([])
    w = SineWindowClass()
    w.show()
    app.exec_()
