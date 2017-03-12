"""How to work with files in the same folder as the main script"""

import os

scriptFolder = os.path.dirname(__file__)
subFolder = "Configs1"
fileName = "AppSettings.json"

fullPath = os.path.join(scriptFolder, subFolder, fileName)
fullPath = os.path.normpath(fullPath)   # Normalize path, eliminating double slashes, etc.

print fullPath, os.path.exists(fullPath)


"""How to work with OS-based user folders"""

print "Home folder on UNIX:", os.getenv('HOME')
print "Folder for user settings on Windows:", os.getenv('APPDATA')  # Like 'C:\Users\Alexey\AppData\Roaming'

print "User folder:", os.path.expanduser('~')   # Like 'C:\Users\Alexey'

import getpass
print "Username:", getpass.getuser()    # Like 'Alexey'


"""How to work with temporary files"""

import tempfile
tmpFolder = tempfile.gettempdir()
print "Temporary folder:", tmpFolder    # Like 'c:\users\alexey\appdata\local\temp'

tmpFile = tempfile.NamedTemporaryFile(delete=False)
print "Temporary file:", tmpFile.name    # Like 'c:\users\alexey\appdata\local\temp\tmpinehhv'
