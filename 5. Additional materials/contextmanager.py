import time
with open('c:/file') as f:
    print f.read()

class timer(object):
    def __enter__(self):
        self.t = time.time()
    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'Time:', time.time() - self.t

with timer():
    for i in range(500000):
        print i

