There is some basic information how to create your application:

1. Use Qt Designer to create ui-files:
- QMainWindow - the main window of the application.
- QDialog - for modal or modeless dialogs.
- QWidget - also for modal or modeless dialogs, if you don't need standard dialog buttons.
  
2. Compile ui-files as py-files (I usually add ending "_UI.py" in order to distinguish them from my py-files).
For PySide and PyQt, respectively:

```Batch
C:\Python27\Scripts\pyside-uic.exe "{0}" -o "{1}"
C:\Python27\Lib\site-packages\PyQt4\pyuic4.bat "{0}" -o "{1}"
```

Here {0} and {1} - names of the ui-file and the compiled py-file ("_UI.py"), respectively.
  
3. Create the main py-file of the application:
-	Import the file "_UI.py" with QMainWindow.
-	Create your class as a subclass of two classes: QMainWindow from PySide.QtGui and the class from the compiled py-file.
-	Add to "\_\_init\_\_" two method calls listed below.
-	Show the main window.

Example:

```python
from PySide.QtGui import *
from widgets import projectManager_UI as ui

class ProjectManagerClass(QMainWindow, ui.Ui_projectManager):
	def __init__(self):
		super(ProjectManagerClass, self).__init__()
		self.setupUi(self)

if __name__ == '__main__':
	app = QApplication([])
	w = ProjectManagerClass()
	w.show()
	app.exec_()
```
  
4. Create py-files for dialogs in the same way as for the main window (except showing them).
Modal dialogs have a parent (the main window or another dialog), but modeless ones don't.
Modal dialog:

```python
class SettingsDialogClass(QDialog, ui.Ui_settingsDialog):
	def __init__(self, parent):
		super(SettingsDialogClass, self).__init__(parent)
		self.setupUi(self)
```

Modeless dialog:

```python
class TemplateEditorClass(QDialog, ui.Ui_templateEditor):
	def __init__(self):
		super(TemplateEditorClass, self).__init__()
		self.setupUi(self)
```
  
5. Create py-files for complex widgets, that will be added on the main window or a dialog window in your code.
It is useful, if the widgets have a lot of related methods.
The code is similar to dialogs, but without calling "self.setupUi(self)" in "\_\_init\_\_", plus you usually don't have a ui-file for them:

```python
class ProjectListClass(QListWidget):
	def __init__(self):
		super(ProjectListClass, self).__init__()
```
  
6. Add your complex widgets on the main window and the dialogs where necessary (you should have a layout for them).
It is done in the "\_\_init\_\_" method:

```python
self.projectList_lwd = projectListWidget.ProjectListClass()
self.projectList_ly.addWidget(self.projectList_lwd)
```
  
7. Make the application work by editing the main window and all dialog py-files:
-	Write your own methods.
-	Connect buttons and other GUI-elements with the methods, that must be called.
-	Open dialogs from the main window or other dialogs (pay attention, that you need to call modal dialogs with "self" and modeless ones without, plus you need to show modeless dialogs manually).

```python
class ProjectManagerClass(QMainWindow, ui.Ui_projectManager):
	def __init__(self):
	super(ProjectManagerClass, self).__init__()
		self.setupUi(self)
	
		# connects
		self.settings_btn.clicked.connect(self.open_settings_dialog)
		self.templateEditor_btn.clicked.connect(self.open_template_editor_dialog)
	
	def open_settings_dialog(self):
		# Modal window
		self.dial = settingsDialog.SettingsDialogClass(self)
	
	def open_template_editor_dialog(self):
		# Modeless window
		self.dial = templateEditor.TemplateEditorClass()
		self.dial.show()
```
  
8. Create a resource file with icons:
-	Create a folder with icons (PNG-files).
-	When editing a widget, e.g. QMainWindow, click View-Resource Browser.
-	Create a new resource file, add prefixes (categories) in it and icons in the prefixes. Save the file (QRC-file).
-	Compile it using "C:\Python27\Lib\site-packages\PySide\pyside-rcc.exe" (pyside-rcc.exe, QRC-file, "-o", PY-file).
  
9. Import the PY-file with resources and set the icons for buttons and so on. Examples (in the "\_\_init\_\_" method):
```python
	self.setWindowIcon(QIcon(':/ico32/appicon.png'))
	self.create_btn.setIcon(QIcon(':/ico32/createproject.png'))
```

10. Context menus for widgets are added in the following way:
-	For a widget, where you want to get a menu, call setContextMenuPolicy(Qt.CustomContextMenu).
-	For the same widget add a connect for a customContextMenuRequested signal to a method creatind a menu.
-	Add a method creating QMenu. Fill the menu, using addAction with QAction.
-	In the same method define a position for the menu to open and execute the menu.  

```python
	def __init__(self):
		self.projectList_lwd.setContextMenuPolicy(Qt.CustomContextMenu)
		self.projectList_lwd.customContextMenuRequested.connect(self.openProjectMenu)
	def openProjectMenu(self, pos):
		pos = self.sender().mapToGlobal(pos)
		menu = QMenu()
		act_update_project = QAction('Update Project', self,
									triggered=(lambda: self.update_project(self.getFocusedProject())))
		menu.addAction(act_update_project)
		menu.exec_(pos)
```

11. Drag'n'drop enabled for a widget in the following way:  
-	setDragDropMode(QAbstractItemView.DragDrop)
-	Special methods: dropEvent, startDrag, dragEnterEvent, dragMoveEvent

12. If you need to transfer a signal from an embedded widget, do the following:
-	Create a custom signal: "mySignal = Signal(object)" before "\_\_init\_\_" method.
-	Emit the custom signal with any arguments: "self.mySignal.emit(arg)"
-	In the enclosing widget connect the signal to a method you want: "self.enclosedWidget.mySignal.connect(self.myMethod)"



