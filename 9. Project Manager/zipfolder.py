#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zipfile
import os

def zipFolder(folder):
    folderRoot, folderName = os.path.split(folder)
    fileName = folderName + '.zip'
    zipFile = os.path.join(folderRoot, fileName)
    zf = zipfile.ZipFile(zipFile, 'w', compression=zipfile.ZIP_DEFLATED, allowZip64=True)
    for path, dirs, files in os.walk(folder):
        for f in files:
            fullPath = os.path.join(path, f)
            relativePath = os.path.relpath(fullPath, folder)
            zf.write(fullPath, relativePath)  # File and its name in the archive
    zf.close()



