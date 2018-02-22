from PySide.QtCore import *
from PySide.QtGui import *
from icons import resources

import os

icon = os.path.join(os.path.dirname(__file__), 'drag.png')

class listWidgetClass(QListWidget):
    def __init__(self):
        super(listWidgetClass, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setDragDropMode(QAbstractItemView.DropOnly)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.files = []

    def dropEvent(self, event):
        """On drop add new rows, only if files are dragging"""
        mimedata = event.mimeData()
        if mimedata.hasUrls():
            for f in mimedata.urls():
                self.addFile(f.toLocalFile())   # Call with path, not QUrl

    def dragEnterEvent(self, event):
        """Called when the cursor gets to the area first"""
        if event.source() is self:  # Forbid dropping on the same widget
            event.ignore()
        else:
            mimedata = event.mimeData()
            if mimedata.hasUrls():
                event.accept()
            else:
                event.ignore()

    def dragMoveEvent(self, event):
        """Called many times while the cursor moving"""
        if event.source() is self:  # Forbid dropping on the same widget
            event.ignore()
        else:
            mimedata = event.mimeData()
            if mimedata.hasUrls():  # How does the cursor look?
                event.accept()
            else:
                event.ignore()

    def addFile(self, path):
        """Add new rows in the list"""
        if not path in self.files:  # Don't add the same file twice
            item = QListWidgetItem(self)
            item.setText(os.path.basename(path))
            item.setData(Qt.UserRole, path)
            item.setToolTip(path)
            if os.path.isdir(path):
                item.setIcon(QIcon(':/ico16/16x16/folder.png'))
            else:
                item.setIcon(QIcon(':/ico16/16x16/image.png'))
            self.files.append(path)

    def deleteSelected(self):
        """Delete rows from the original widget"""
        for s in self.selectedItems():
            self.files.remove(s.data(32))
            self.takeItem(self.indexFromItem(s).row())

    def getAllFiles(self):
        return self.files

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.deleteSelected()