set UIFILE=%1
set UIDIR=%~dp$PATH:1
set FILENAME=%~n1
set NNAME=%UIDIR%%FILENAME%_UI_pyqt.py
set SNAME=%UIDIR%%FILENAME%_UI.py

CALL C:\Python27\Lib\site-packages\PyQt4\pyuic4.bat %UIFILE% -o "%NNAME%"
CALL C:\Python27\Scripts\pyside-uic.exe %UIFILE% -o "%SNAME%"

set /p Done="Press any key to exit"
