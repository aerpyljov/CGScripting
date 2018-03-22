from PySide.QtGui import *
from PySide.QtCore import *

class simpleWidget(QWidget):
    def __init__(self):
        super(simpleWidget, self).__init__()
        ly = QVBoxLayout(self)
        self.label = QLabel('Start')
        ly.addWidget(self.label)
        self.installEventFilter(self) # Activate a filter. Call with an instance of a class with 'eventFilter' method
        # self.removeEventFilter(self) # Deactivate a filter
        
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            self.label.setText('In')
            return True # Event processed
        elif event.type() == QEvent.Leave:
            self.label.setText('Out')
            return True
        return False # Send event to the widget


if __name__ == '__main__':
    app = QApplication([])
    w = simpleWidget()
    w.show()
    app.exec_()
