from PySide.QtCore import *
from PySide.QtGui import *
import window_UIs

class exampleWindowClass(QWidget, window_UIs.Ui_example):   # Inherited from the class created in Qt Designer
    def __init__(self):
        super(exampleWindowClass, self).__init__()
        self.setupUi(self)  # Obligatory!
        self.setWindowTitle('ITEM LIST')
        self.count = 1
        self.additem_btn.clicked.connect(self.addItem)  # If the button is clicked
        self.name_le.returnPressed.connect(self.addItem)    # If the ENTER button pressed

    def addItem(self):
        text = self.name_le.text()
        if text:
            lb = QLabel('%s: %s' %(self.count,text))
            self.items_ly.addWidget(lb)
            self.count += 1

if __name__ == '__main__':
    app = QApplication([])
    w = exampleWindowClass()
    w.show()
    app.exec_()
