# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\projects\pyqt\week3\icon_widget\iconWidget.ui'
#
# Created: Wed Oct 15 18:38:42 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(237, 369)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.fill_btn = QtGui.QPushButton(self.centralwidget)
        self.fill_btn.setObjectName(_fromUtf8("fill_btn"))
        self.horizontalLayout.addWidget(self.fill_btn)
        self.clear_btn = QtGui.QPushButton(self.centralwidget)
        self.clear_btn.setMinimumSize(QtCore.QSize(40, 0))
        self.clear_btn.setObjectName(_fromUtf8("clear_btn"))
        self.horizontalLayout.addWidget(self.clear_btn)
        self.image_lb = QtGui.QLabel(self.centralwidget)
        self.image_lb.setObjectName(_fromUtf8("image_lb"))
        self.horizontalLayout.addWidget(self.image_lb)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.combo_cbb = QtGui.QComboBox(self.centralwidget)
        self.combo_cbb.setObjectName(_fromUtf8("combo_cbb"))
        self.verticalLayout.addWidget(self.combo_cbb)
        self.list_lwd = QtGui.QListWidget(self.centralwidget)
        self.list_lwd.setObjectName(_fromUtf8("list_lwd"))
        self.verticalLayout.addWidget(self.list_lwd)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 237, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menuBar)
        self.fill_act = QtGui.QAction(MainWindow)
        self.fill_act.setObjectName(_fromUtf8("fill_act"))
        self.clear_act = QtGui.QAction(MainWindow)
        self.clear_act.setObjectName(_fromUtf8("clear_act"))
        self.open_act = QtGui.QAction(MainWindow)
        self.open_act.setObjectName(_fromUtf8("open_act"))
        self.save_act = QtGui.QAction(MainWindow)
        self.save_act.setObjectName(_fromUtf8("save_act"))
        self.exit_act = QtGui.QAction(MainWindow)
        self.exit_act.setObjectName(_fromUtf8("exit_act"))
        self.toolBar.addAction(self.fill_act)
        self.toolBar.addAction(self.clear_act)
        self.menuFile.addAction(self.open_act)
        self.menuFile.addAction(self.save_act)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.exit_act)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.fill_btn.setText(_translate("MainWindow", "Fill", None))
        self.clear_btn.setText(_translate("MainWindow", "Clear", None))
        self.image_lb.setText(_translate("MainWindow", "TextLabel", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.fill_act.setText(_translate("MainWindow", "Fill", None))
        self.clear_act.setText(_translate("MainWindow", "Clear", None))
        self.open_act.setText(_translate("MainWindow", "Open", None))
        self.save_act.setText(_translate("MainWindow", "Save", None))
        self.exit_act.setText(_translate("MainWindow", "Exit", None))

