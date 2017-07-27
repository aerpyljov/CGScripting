#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os, sys, subprocess, shutil
import settings

def zipFolder(old_path, new_path):
    if sys.platform == 'win32':
        winEncoding = settings.SettingsClass().load()['winEncoding']
        old_path = old_path
        archiver_folder = os.path.dirname(os.path.abspath(__file__))
        archiver = os.path.join(archiver_folder, '7zr.exe')
        archive_name = (new_path + '.7z')
        # subprocess.call([archiver, 'a', '-bd', '-y', archive_name, old_path])
        command = r'"{0}" a -bd -y "{1}" "{2}"'.format(archiver, archive_name, old_path)
        subprocess.call(command.encode(winEncoding))
    else:
        shutil.make_archive(new_path, 'zip', old_path)
