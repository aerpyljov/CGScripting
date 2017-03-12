import os
p = os.path.normpath(os.path.join(os.path.dirname( __file__ ), 'folder', 'objects'))
print p, os.path.exists(p)
######################
os.getenv('HOME')
os.path.expanduser('~')
import getpass
getpass.getuser()
#######################
os.getenv('APPDATA')
#######################
import tempfile
tempfile.gettempdir()
f = tempfile.NamedTemporaryFile(delete=False)
print f.name

import script2
script2.__dict__