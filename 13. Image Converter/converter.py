import os, subprocess, locale

ENCODING = locale.getpreferredencoding()


def convert(imageMagickPath, src, trg_ext, trg=None, overwrite=False):
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
        try:
            src_enc = src.encode(ENCODING)
            trg_enc = trg.encode(ENCODING)
            exe_enc = imageMagickPath.encode(ENCODING)
            subprocess.Popen([exe_enc, src_enc, trg_enc])
        except Exception as E:
            print('Src = ' + src)
            print('Trg = ' + trg)
            print('Exception = ' + str(E) + '\n')
