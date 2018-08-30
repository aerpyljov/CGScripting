from PySide.QtCore import *
from PySide.QtGui import *
import sceneWidget

class exampleViewClass(QGraphicsView):
    def __init__(self):
        super(exampleViewClass, self).__init__()
        self.s = sceneWidget.exampleSceneClass()
        self.setScene(self.s)
        self.s.setSceneRect(-200, -200, 400, 400)
        self.item = self.s.addRect(0, 0, 30, 30, QPen(Qt.black), QBrush(Qt.red))
        self.item.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.item = self.s.addRect(40, 40, 30, 30, QPen(Qt.black), QBrush(Qt.red))
        self.item.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)



if __name__ == '__main__':
    app = QApplication([])
    w = exampleViewClass()
    w.show()
    app.exec_()
