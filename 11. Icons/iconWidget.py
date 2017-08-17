from PySide.QtCore import *
from PySide.QtGui import *
import  iconWidget_UIs as ui
from icons.icons import icons
import random, os
import ctypes
from icons import icons_rcs
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')


class iconWidgetClass(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(iconWidgetClass, self).__init__()
        self.setupUi(self)
        # ui
        self.setWindowIcon(QIcon(icons['create']))
        self.fill_btn.setText('')
        self.fill_btn.setFixedSize(QSize(40,40))
        self.fill_btn.setIconSize(QSize(32,32))
        self.fill_btn.setFlat(1)
        # self.fill_btn.setIcon(QIcon(icons['create']))
        self.fill_btn.setIcon(QIcon(':/create.png'))
        self.clear_btn.setText('')
        self.clear_btn.setFixedSize(QSize(40,40))
        self.clear_btn.setIconSize(QSize(32,32))
        self.clear_btn.setFlat(1)
        self.clear_btn.setIcon(QIcon(icons['clear']))

        self.fill_act.setIcon(QIcon(icons['create']))
        self.clear_act.setIcon(QIcon(icons['clear']))
        self.open_act.setIcon(QIcon(icons['open']))
        self.save_act.setIcon(QIcon(icons['save']))
        self.exit_act.setIcon(QIcon(icons['close']))

        pix = QPixmap(icons['sphere']).scaled( 40, 40,
                                               Qt.KeepAspectRatio,
                                               Qt.SmoothTransformation )
        self.image_lb.setPixmap(pix)

        self.list_lwd.setViewMode(QListView.IconMode)
        self.list_lwd.setIconSize(QSize(64,64))
        self.list_lwd.setResizeMode(QListWidget.ResizeMode.Adjust)
        self.list_lwd.setDragDropMode(QAbstractItemView.NoDragDrop)

        #connects
        self.fill_btn.clicked.connect(self.filList)
        self.clear_btn.clicked.connect(self.clearList)
        self.fill_act.triggered.connect(self.fillCombo)
        self.clear_act.triggered.connect(self.clearCombo)


    def filList(self):
        path = os.path.join(os.path.dirname(__file__), 'textures')
        self.clearList()
        for i in os.listdir(path):
            item = QListWidgetItem(i)
            item.setIcon( QIcon( os.path.join(path, i) ) )
            self.list_lwd.addItem(item)
    def clearList(self):
        self.list_lwd.clear()

    def fillCombo(self):
        self.clearCombo()
        for i in range(10):
            self.combo_cbb.addItem('Item %s' % i)
            self.combo_cbb.setItemIcon(i, self.getRandomIcon())
    def clearCombo(self):
        self.combo_cbb.clear()

    def getRandomIcon(self):
        return QIcon(icons[random.choice(['item1','item2','item3'])])

if __name__ == '__main__':
    app = QApplication([])
    w = iconWidgetClass()
    w.show()
    app.exec_()