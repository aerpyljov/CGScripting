"""
In order to test the script, run it in a folder with the following test data:
- Folder 'To be packed', containing a file 'file.txt' with some text and any other subfolders and files.

Advice for real life use:
- When you create a ZIP-archive, check, that the archive isn't in a folder to be packed.
"""


import zipfile
import os

"""How to create a ZIP-archive from a file"""
scriptFolder = os.path.dirname(__file__)
srcFolder = os.path.join(scriptFolder, 'To be packed')
srcFile = os.path.join(srcFolder, 'file.txt')
zFile = os.path.join(scriptFolder, 'archive.zip')

zf = zipfile.ZipFile(zFile, 'w', compression=zipfile.ZIP_DEFLATED, allowZip64=True)
# Compressed archive, archives larger than 2GB allowed

zf.write(srcFile, os.path.basename(srcFile))    # File and its name in the archive
zf.close()


"""How to create a ZIP-archive from a folder"""
zf = zipfile.ZipFile(zFile, 'w', compression=zipfile.ZIP_DEFLATED, allowZip64=True)
for path, dirs, files in os.walk(srcFolder):
    for f in files:
        fullPath = os.path.join(path, f)
        relativePath = os.path.relpath(fullPath, srcFolder)
        zf.write(fullPath, relativePath)    # File and its name in the archive
zf.close()


"""How to unpack a ZIP-archive into a target folder"""
trg = os.path.join(scriptFolder, 'Unpacked')
zf = zipfile.ZipFile(zFile, 'r')
for f in zf.namelist():
    full = os.path.join(trg, f)
    d = os.path.dirname(full)
    if d:   # For folders in the ZIP-archive
        if not os.path.exists(d):
            os.makedirs(d)
    if os.path.basename(f):   # For files in the ZIP-archive
        out = open(full, 'wb')
        out.write(zf.read(f))
        out.close()
zf.close()
