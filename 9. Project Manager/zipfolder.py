#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os, sys, subprocess, shutil
import settings

def zipFolder(old_path, new_path):
    if sys.platform == 'win32':
        win_encoding = settings.SettingsClass().load()['winEncoding']
        archiver_folder = os.path.dirname(os.path.abspath(__file__))
        archiver = os.path.join(archiver_folder, '7zr.exe')
        archive_name = (new_path + '.7z')
        command = r'"{0}" a -bd -y "{1}" "{2}"'.format(archiver, archive_name, old_path)
        subprocess.call(command.encode(win_encoding))
    else:
        shutil.make_archive(new_path, 'zip', old_path)
