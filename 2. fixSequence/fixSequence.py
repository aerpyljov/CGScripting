#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The script can help you, if you have a lot of photos, and every name has digits in the end.
The script allows you to achieve the following goals:
- Put photos from different cameras into different folders.
- Rename the photos: change the word (the sequence name) and the sequence number (start from 1, add padding).
- Create a file with statistics
- Delete original files

Requirements:
- Python 2.7.
- A folder with files (usually photos).
- Every file must have a name, consisting of two parts: (1) one or more non-digits and (2) one or more digits.
For example: 'photo-12.jpg'.
The second part will be converted as a number, so it must be unique for all files with the same first parts: 
you can't have both files with names like 'photo01' and 'photo1', because after the conversion '01' will be equal to '1'.
The second part after the conversion must be 1 or more, not 0.


How to use:
- Drag and drop the folder with all photos on the script.
- Enter new sequence names for each sequence in English or Russian.
- Answer, whether you want to delete the original files or not.


What is different from the example:
- It works for more than 1 sequence.
- The folder with photos isn't a part of the script.
- New sequence names aren't parts of the script.
- It creates a file with statistics.
- The name of the folder with photos can be not only in English, but in Russian too.
- Original names of the photos can be not only in English, but in Russian too.
- New names of the photos can be not only in English, but in Russian too.
- Different operating systems are supported 
(tested with MS Windows (Russian regional and language settings) and Linux).
"""


import os
import sys
import shutil


# USER SETTINGS

CONSOLE_ENCODING = 'cp866'    # Use 'cp866' for Windows (Russian), 'utf-8' for UNIX
FILEPATH_ENCODING = 'cp1251'    # Use 'cp1251' for Windows (Russian), 'utf-8' for UNIX
TXT_ENCODING = 'cp1251'    # Use 'cp1251' for Windows (Russian), 'utf-8' for UNIX

padding = 4


# Define functions
def getListOfFiles(folder):
    "Return a list of files in a folder (not subfolders)"
    tmp = os.listdir(folder)
    files = []
    for t in tmp:
        if os.path.isfile( os.path.join(folder, t) ):
            files.append(t)
    return files

    
def getSequences(files):
    "Return a set of sequences (a list of unique first parts of file names, before frame number)"
    sequences = []
    for f in files:
        name, ext = os.path.splitext(f)
        while name[-1].isdigit():
            name = name[:-1]
        sequences.append(name)
    sequences = set(sequences)
    return sequences
    

def getNewSequenceNames(sequences):
    "Ask the user to enter new names for each sequence and return them as values of a dictionary (old names are keys)"
    newSequenceNames = dict.fromkeys(sequences)
    usedSequenceNames = ""
    for s in sequences:
        print s
        message = """Enter a new name for a sequence with name "{0}".\nYou have already used these names: {1}.\n
        Type new name: """.format(s.encode(CONSOLE_ENCODING), usedSequenceNames.encode(CONSOLE_ENCODING))
        rawNewSequenceName = raw_input(message).decode(CONSOLE_ENCODING)
        while unicode(rawNewSequenceName) in newSequenceNames.values():
            message = """Sorry, the name "{0}" is already used. """.format(rawNewSequenceName.encode(CONSOLE_ENCODING)) + message
            rawNewSequenceName = raw_input(message).decode(CONSOLE_ENCODING)
        newSequenceName = rawNewSequenceName
        newSequenceNames[s] = newSequenceName
        usedSequenceNames += newSequenceName + ", " 
    return newSequenceNames


def makeFoldersForSequences(path, newSequenceNames):
    "Make one folder for each sequence in the folder with files"
    for s in newSequenceNames:
        newSequenceName = newSequenceNames[s]
        outFolder = os.path.join(path, newSequenceName)
        if not os.path.exists(outFolder):
            os.mkdir(outFolder)


def getListOfFilesForSequence(files, sequence):
    "Return a list of files with the sequence name"
    sequenceFiles = []
    for f in files:
        if f.startswith(sequence):
            sequenceFiles.append(f)
    return sequenceFiles     
            
            
def getFrames(sequenceFiles):
    "Return a list of frames based on a list of files"
    frames = []
    for f in sequenceFiles:
        name, ext = os.path.splitext(f)
        fullName = name
        while name[-1].isdigit():
            name = name[:-1]
        digits = int(fullName.replace(name, ''))
        frames.append(digits)
    return frames        

    
def getOffset(frames):
    "Return an offset as a digit based on a list of frames"
    offset = min(frames) - 1
    return offset

    
def getMissingFrames(frames):
    "Return missing frames as list of strings based on a list of frames"
    fullrange = range(min(frames), max(frames)+1)
    missFrames = []
    for i in fullrange:
        if not i in frames:
            i = str(i)
            missFrames.append(i)        
    return missFrames

    
def copySequence(path, sequenceFiles, newSequenceName, offset, padding):
    for i, f in enumerate(sequenceFiles):
        old = os.path.join(path, f)
        name, ext = os.path.splitext(f)
        newName = newSequenceName + '_' + str(frames[i]-offset).zfill(padding) + ext
        new = os.path.join(path, newSequenceName, newName)
        if os.path.exists(new):
            os.remove(new)
        shutil.copy2(old, new)    

        



    
# Find the name of the folder with photos for renaming
path = sys.argv[1]
path = path.decode(FILEPATH_ENCODING)


# Find sequences, ask the user to enter new names for sequences and make a folder for each sequence with new name
files = getListOfFiles(path)

sequences = getSequences(files)

newSequenceNames = getNewSequenceNames(sequences)

makeFoldersForSequences(path, newSequenceNames)


# For each sequence: copy the sequence and rename files. Plus make a file with statistics.
numFiles = len(files)
numSequences = len(sequences)
statistics = \
"""All files: {0}\n
Sequences: {1}\n
Info by sequences: original name, new name, number of files, missing frames:\n
""".format(numFiles, numSequences)

for s in newSequenceNames:
    sequenceFiles = getListOfFilesForSequence(files, s)
    numFilesInSequence = len(sequenceFiles)
    frames = getFrames(sequenceFiles)
    missFrames = getMissingFrames(frames)
    missFrames = ", ".join(missFrames)
    offset = getOffset(frames)
    newSequenceName = newSequenceNames[s]
    copySequence(path, sequenceFiles, newSequenceName, offset, padding)
    statisticsInfo = "- {0} -> {1}: {2} files (missing frames: {3})\n"\
                        .format(s.encode(TXT_ENCODING), newSequenceName.encode(TXT_ENCODING), numFilesInSequence, missFrames)
    statistics += statisticsInfo

filename = os.path.join(path, "statistics.txt")
file = open(filename, 'w')
file.write(statistics)
file.close()



# Delete original files and add the result message to the statistics
a = raw_input('Remove old files? [y/n]: ')
if a == 'y' or a == 'Y':
    for f in files:
        os.remove(os.path.join(path, f))
    result = "DELETED"
else:
    result = "NOT deleted"
resultMessage = "\nOriginal files were {0}.".format(result)

filename = os.path.join(path, "statistics.txt")
file = open(filename, 'a')
file.write(resultMessage)
file.close()

print 'Complete!'
raw_input()



