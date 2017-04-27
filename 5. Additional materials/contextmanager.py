import time

"""The file will be closed automatically"""
with open('c:/file') as f:
    print f.read()


"""This class can be used with a context manager: some actions will be done before and after the main action"""
class timer(object):
    def __enter__(self):
        self.t = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'Time:', time.time() - self.t, 'seconds'


with timer():
    for i in range(5000):
        print i
