import os, subprocess

imageMagick = r"C:\Users\Alexey\Documents\GitHub\CGScripting\13. Image Converter\ImageMagick\magick.exe"


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
    subprocess.Popen([imageMagick, src, trg])
