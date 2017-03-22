set UIFILE=%1
set UIDIR=%~dp1
set FILENAME=%~n1
set PQTNAME=%UIDIR%%FILENAME%_ui.py
set PSDNAME=%UIDIR%%FILENAME%_uis.py
CALL C:\Python27\Lib\site-packages\PyQt4\pyuic4.bat %UIFILE% -o %PQTNAME%
CALL C:\Python27\Scripts\pyside-uic.exe %UIFILE% -o %PSDNAME%
