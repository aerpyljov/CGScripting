There is some basic information how to create your application:

1. Use Qt Designer to create ui-files:
- QMainWindow - the main window of the application.
- QDialog - for modal or modeless dialogs.
- QWidget - for widgets, that will be added on the main window or a dialog window in your code.

2. Compile ui-files as py-files (I usually add ending "_UI.py" in order to distinguish them from my py-files).
For PySide:
	C:\Python27\Scripts\pyside-uic.exe "{0}" -o "{1}"
For PyQt:
	C:\Python27\Lib\site-packages\PyQt4\pyuic4.bat "{0}" -o "{1}"
Here:
{0} - Name of the ui-file.
{1} - Name of the compiled py-file ("_UI.py").

3. Create the main py-file of the application:
-	Import the file "_UI.py" with QMainWindow.
-	Create your class as a subclass of two classes: QMainWindow from PySide.QtGui and the class from the compiled py-file.
-	Add to "__init__" two method calls listed below.
-	Show the main window.

Example:

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


4. 
-	Write your own methods.
-	Connect buttons and other GUI-elements with the methods, that must be called.