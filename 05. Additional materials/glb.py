import glob
import os


p = 'c:/windows'

"""Find all EXE-files using a list generator"""
e = [x for x in os.listdir(p) if os.path.isfile(os.path.join(p, x)) and os.path.splitext(x)[-1] == '.exe']
print e

"""Find all EXE-files with names ending with a digit, using 'glob' module"""
print glob.glob1(p, '*[0-9].exe')
