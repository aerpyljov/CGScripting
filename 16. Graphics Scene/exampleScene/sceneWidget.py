from PySide.QtCore import *
from PySide.QtGui import *


class exampleSceneClass(QGraphicsScene):
    def __init__(self):
        super(exampleSceneClass, self).__init__()

    def drawBackground(self, painter, rec):
        painter.setPen(QPen(Qt.green, 3))
        painter.drawRect(self.sceneRect())
        painter.setPen(QPen(Qt.black))
        painter.drawText(0, 0, '0')
        painter.drawText(-200, -200, '-200')
        painter.drawText(200, 200, '200')



if __name__ == '__main__':
    app = QApplication([])
    w = exampleSceneClass()
    w.show()
    app.exec_()
