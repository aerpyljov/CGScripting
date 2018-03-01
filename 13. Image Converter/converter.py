import os, subprocess

imageMagick = r"C:\Users\Alexey\Documents\GitHub\CGScripting\13. Image Converter\ImageMagick\magick.exe"


def convert(src, trg_ext, trg=None, overwrite=False):
    if trg:
        if not os.path.exists(trg):
            os.makedirs(trg)
        elif os.path.isfile(trg):
            trg = os.path.dirname(trg)
        basename = os.path.basename(src)
        name, ext = os.path.splitext(basename)
        trg = os.path.join(trg, name + '.' + trg_ext)
    else:
        trg = os.path.splitext(src)[0] + '.' + trg_ext
    if not overwrite and os.path.exists(trg):
        pass
    else:
        subprocess.Popen([imageMagick, src, trg])
