import os

imageMagick = r"C:\Users\Alexey\Documents\GitHub\CGScripting\13. Image Converter\ImageMagick\magick.exe"
imageMagick = '"' + imageMagick + '"'

def convert(src, trg=None):
    if trg:
        if not os.path.exists(trg):
            os.makedirs(trg)
        elif os.path.isfile(trg):
            trg = os.path.dirname(trg)
        basename = os.path.basename(src)
        name, ext = os.path.splitext(basename)
        trg = os.path.join(trg, name + '.png')
    else:
        trg = os.path.splitext(src)[0] + '.png'
    src = '"' + src + '"'
    trg = '"' + trg + '"'
    cmd = ' '.join([imageMagick, src, trg])
    print cmd
    os.popen(cmd)
    print cmd

convert(r"C:\Users\Alexey\Pictures\ship.jpg")
