#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, subprocess, shutil

def zipFolder(old_path, new_path):
    if sys.platform == 'win32':
        archiver_folder = os.path.dirname(os.path.abspath(__file__))
        archiver = os.path.join(archiver_folder, '7zr.exe')
        archive_name = new_path + '.7z'
        subprocess.call([archiver, 'a', '-bd', '-y', archive_name, old_path])
        subprocess.call([archiver, 'a', '-bd', '-y', archive_name, old_path])
    else:
        shutil.make_archive(new_path, 'zip', old_path)



