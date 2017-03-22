All scripts are provided as parts of the course, but I amended them a bit and added some comments.

- "simpleWidget.py" - a window with a label and a button, that do nothing.
- "simpleClassWidget.py" - the same simple widget, but defined as a class.
- "connect.py" - working with signals and slots. Example: an action when a button is clicked.
- "compile_ui" - BAT-scripts for creating Python files (.py) from Qt Designer files (.ui), using PyQt or PySide. Drag an UI-file and drop it on a BAT-file.
- "changeText.py" - the course author's example how to change a label when a button is clicked.

Some of the examples are completely rewritten:

- "connect.py" - originally the script just printed some text in the console, but now it displays the text user typed in the widget itself. Plus non-English text support added.



NB: Pay attention, that you need to install PySide first:
http://wiki.qt.io/PySideDownloads
