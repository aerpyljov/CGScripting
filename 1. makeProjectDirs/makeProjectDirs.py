#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
The script allows you to create a folder tree.
It is useful, if you have to create folders for different projects with the same sub-folders regularly.

Requirements:
- MS Windows with Russian regional and language settings.
- Python 2.7.
- TXT-file, describing a folder tree (encoding cp1251).

How to use:
- Put the TXT-file in a folder, where you want to create a project folder.
- Drag and drop the TXT-file on the script.
- Enter the project name in English or Russian.

What is different from the example:
- The folder tree isn't a part of the script.
- The root folder for the project isn't a part of the script.
- Folder names can be not only in English, but in Russian too.
- A project name can be not only in English, but in Russian too.

What I haven't managed to do:
- I wanted to use a user-friendly format for TXT-file (with TAB to make a folder tree),
but I had to use a list (Python data structure).
'''


import os
import sys
import ast
import codecs

# Get file name and its folder to use as the folder for the project
filePath = sys.argv[1]
path = os.path.dirname(filePath)


# Get the folder from the file (Russian names also can be used)
foldersAsText = codecs.open(filePath, encoding='cp1251').read()
folders = ast.literal_eval(foldersAsText)



def createFolder(path):
    "Create a folder if it doesn't exist"
    if not os.path.exists(path):
        os.mkdir(path)


def build(root, data):
    "Create folders recursively in the root folder"
    if data:
        for d in data:
            rawName = d[0]
            name = rawName.decode('utf-8')
            path = os.path.join(root, name)
            createFolder(path)
            build(path, d[1])

# Ask the user to enter a project name and use it as a root folder for all folders, described in the file
# (a Russian name also can be used)
projectname = raw_input('Enter project name: ').decode('cp866')
if projectname:
    fullPath = os.path.join(path, projectname)
    createFolder(fullPath)
    build(fullPath, folders)

print 'Complete!'
raw_input()
  