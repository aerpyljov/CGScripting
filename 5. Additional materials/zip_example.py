from zipfile import ZipFile
import os

src = 'C:/tmp/data/file.txt'
zFile = 'C:/tmp/archive.zip'
# zf = ZipFile(zFile, 'w')
# zf.write(src, os.path.basename(src))
# zf.close()

trg = 'C:/tmp'
zf = ZipFile(zFile, 'r')
for f in zf.namelist():
    full = os.path.join(trg, f)
    d = os.path.dirname(full)
    if d:
        if not os.path.exists(d):
            os.makedirs(d)
    if os.path.basename(f):
        out = open(full, 'wb')
        out.write(zf.read(f))
        out.close()
zf.close()

folder = 'c:/tmp'
zf = ZipFile('c:/tmp/archive.zip', 'w')

for path, dirs, files in os.walk(folder):
    for file in files:
        full = os.path.join(path, file)
        zf.write(full)
zf.close()

os.path.splitext('c:/file.txt')
