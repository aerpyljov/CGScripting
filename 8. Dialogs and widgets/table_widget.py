from PySide.QtGui import *
from PySide.QtCore import *
import os
path = os.path.dirname(__file__)

class simpleWindow(QWidget):
    path = os.path.dirname(__file__)
    def __init__(self):
        super(simpleWindow, self).__init__()
        ly = QHBoxLayout()
        self.setLayout(ly)
        self.table = QTableWidget()
        ly.addWidget(self.table)
        self.table.verticalHeader().hide()
        self.table.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        # start
        self.resize(500,400)
        self.fillTable()

    def fillTable(self):
        files = os.listdir(path)
        self.table.setColumnCount(2)
        self.table.setRowCount(len(files))
        self.table.setHorizontalHeaderLabels(['Name', 'Size'])
        for i, f in enumerate(files):
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item.setText(f)
            self.table.setItem(i, 0, item)
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item.setText(str(os.stat(os.path.join(path, f)).st_size) + ' bytes' )
            self.table.setItem(i, 1, item)


if __name__ == '__main__':
    app = QApplication([])
    w = simpleWindow()
    w.show()
    app.exec_()
    