There is some basic information how to create your application:

1. Use Qt Designer to create ui-files:
- QMainWindow - the main window of the application.
- QDialog - for modal or modeless dialogs.


2. Compile ui-files as py-files (I usually add ending "_UI.py" in order to distinguish them from my py-files).
For PySide and PyQt, respectively:


	C:\Python27\Scripts\pyside-uic.exe "{0}" -o "{1}"
	C:\Python27\Lib\site-packages\PyQt4\pyuic4.bat "{0}" -o "{1}"

Here:

	{0} - Name of the ui-file.
	{1} - Name of the compiled py-file ("_UI.py").


3. Create the main py-file of the application:
-	Import the file "_UI.py" with QMainWindow.
-	Create your class as a subclass of two classes: QMainWindow from PySide.QtGui and the class from the compiled py-file.
-	Add to "\_\_init\_\_" two method calls listed below.
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


4. Create py-files for dialogs in the same way, as for the main window (except showing them).
Modal dialogs have a parent (the main window or another dialog), but modeless ones don't.
Modal dialog:


	class SettingsDialogClass(QDialog, ui.Ui_settingsDialog):
		def __init__(self, parent):
			super(SettingsDialogClass, self).__init__(parent)
			self.setupUi(self)

Modeless dialog:

	class TemplateEditorClass(QDialog, ui.Ui_templateEditor):
		def __init__(self):
			super(TemplateEditorClass, self).__init__()
			self.setupUi(self)


5. Create py-files for complex widgets, that will be added on the main window or a dialog window in your code.
It is useful, if the widgets wave a lot of related methods.
The code is similar to dialogs, but without calling "self.setupUi(self)" in "\_\_init\_\_", plus you usually don't have a ui-file for them:

	class ProjectListClass(QListWidget):
		def __init__(self):
			super(ProjectListClass, self).__init__()


6. Add your complex widgets on the main window and the dialogs where necessary (you should have a layout for them).
It is done in the "\_\_init\_\_" method:

	self.projectList_lwd = projectListWidget.ProjectListClass()
	self.projectList_ly.addWidget(self.projectList_lwd)


7. Make the application work by editing the main window and all dialog py-files:
-	Write your own methods.
-	Connect buttons and other GUI-elements with the methods, that must be called.
-	Open dialogs from the main window or other dialogs (pay attention, that you need to call modal dialogs with "self" and modeless ones without, plus you need to show modeless dialogs manually).


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

