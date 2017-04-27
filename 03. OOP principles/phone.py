class phone(object):
    def __init__(self):
        self.model = ''
        self.color = 'red'

    def call(self):
        return 'Call'

class phone2(phone):
    def __init__(self):
        super(phone2, self).__init__()

    def sendMail(self):
        pass

    def call(self):
        if False:
            pass
        else:
            return super(phone2, self).call() + ' phone2'

p = phone2()

print p.call()
