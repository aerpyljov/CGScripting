from PySide.QtCore import *
from PySide.QtGui import *


class mainWindowClass(QMainWindow):
    def __init__(self):
        super(mainWindowClass, self).__init__()
        # widget
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        # menu bar
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)
        # menu
        self.menu = QMenu('File')
        self.menu.setTearOffEnabled(1)
        self.menu_bar.addMenu(self.menu)
        # actions
        self.act1 = QAction('Open', self)
        self.act1.setCheckable(1)
        self.act1.triggered.connect(self.action)
        self.menu.addAction(self.act1)
        self.menu.addAction( QAction('Save', self, triggered=self.action) )
        # submenu
        self.sMenu = QMenu('Sub')
        self.menu.addMenu(self.sMenu)

        for i in range(10):
            self.sMenu.addAction( QAction('Item %s' % i, self,
                                          triggered=lambda x=i:self.action(x)))


    def action(self, i):
        print i

if __name__ == '__main__':
    app = QApplication([])
    w = mainWindowClass()
    w.show()
    app.exec_()