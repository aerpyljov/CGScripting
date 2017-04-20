from PySide.QtGui import *
import os
path = os.path.dirname(__file__)

class simpleWindow(QWidget):
    def __init__(self):
        super(simpleWindow, self).__init__()
        ly = QHBoxLayout()
        self.setLayout(ly)
        self.list = QListWidget()
        ly.addWidget(self.list)
        self.textBrowser = QTextBrowser()
        ly.addWidget(self.textBrowser)
        # connect
        self.list.itemClicked.connect(self.updateText)
        self.list.itemDoubleClicked.connect(self.openFile)
        # start
        self.resize(500,400)
        self.fillList()

    def fullPath(self, item):
        return os.path.join(path,item.text())

    def fillList(self):
        for f in os.listdir(path):
            self.list.addItem(f)

    def updateText(self, item):
        text =open(self.fullPath(item)).read()
        self.textBrowser.setText(text)

    def openFile(self, item):
        path = self.fullPath(item)
        os.system(path)


if __name__ == '__main__':
    app = QApplication([])
    w = simpleWindow()
    w.show()
    app.exec_()
    