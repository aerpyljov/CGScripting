The script allows you to read and write settings of an application.
There are the following settings:
- "CultureCode" - like 'ru' or 'ru-RU', obligatory.
- "Servers" - a non-empty dictionary of servers, where each server is described by the following attributes:
    - "ID" - a dictionary key - unique, obligatory.
    - "ServerName" - obligatory.
    - "ServerPort" - obligatory.
    - "UserName" - optional (if not specified, a user must enter it when runs the application).
    - "Password" - optional (if not specified, a user must enter it when runs the application).

It is recommended to run the script in a console, not by a double mouse click.

---------------------------------

"Examples" folder contains scripts provided as parts of the course, without any changes from me.

- "settings.py" - How to make a simple class for writing and reading application settings by TXT-file.
- "json_example.py" - How to work with JSON.
- "xml_example.py" - How to work with XML.
