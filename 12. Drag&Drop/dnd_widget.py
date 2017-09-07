from PySide.QtCore import *
from PySide.QtGui import *

import os

icon = os.path.join(os.path.dirname(__file__), 'drag.png')

class listWidgetClass(QListWidget):
    def __init__(self):
        super(listWidgetClass, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setDragDropMode(QAbstractItemView.DragDrop)
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

    def startDrag(self, dropAction):
        """Create MIME data when dragging and add an icon to the cursor"""
        drag = QDrag(self)
        mimedata = QMimeData()
        url = []
        for i in self.selectedItems():
            url.append(i.data(Qt.UserRole))
        mimedata.setUrls([QUrl.fromLocalFile(x) for x in url])  # Paths to QUrls
        drag.setMimeData(mimedata)
        pix = QPixmap(icon) # Custom icon near the cursor
        drag.setPixmap(pix)
        r = drag.exec_()
        if r == Qt.DropAction.MoveAction:   # Only if dropped where allowed
            self.deleteSelected()

    def addFile(self, path):
        """Add new rows in the list"""
        if not path in self.files:  # Don't add the same file twice
            item = QListWidgetItem(self)
            item.setText(os.path.basename(path))
            item.setData(Qt.UserRole, path)
            self.files.append(path)

    def deleteSelected(self):
        """Delete rows from the original widget after dropping on another widget"""
        for s in self.selectedItems():
            self.files.remove(s.data(32))
            self.takeItem(self.indexFromItem(s).row())

    def mousePressEvent(self, event):
        """Forbid dragging by the left mouse button"""
        if event.button() == Qt.MouseButton.RightButton:
            pass
        elif event.button() == Qt.MouseButton.LeftButton:
            self.setDragDropMode(QAbstractItemView.NoDragDrop)
            super(listWidgetClass, self).mousePressEvent(event) # Standard effect allowed
        else:
            self.setDragDropMode(QAbstractItemView.DragDrop)
            super(listWidgetClass, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        """Restore DragDrop mode after the left mouse button released"""
        self.setDragDropMode(QAbstractItemView.DragDrop)
        super(listWidgetClass, self).mouseReleaseEvent(event)

if __name__ == '__main__':
    app = QApplication([])
    w = listWidgetClass()
    w.show()
    app.exec_()