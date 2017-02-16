

import os

class settings():
    def __init__(self, path=None):
        if path:
            self.path = path
        else:
            self.path = 'c:/settings.ini'
        self.data = self.__readFile()

    def __readFile(self):
        if os.path.exists(self.path):
            text = open(self.path, 'r').readlines()
            data = {}
            if text:
                for line in [x.strip() for x in text]:
                    key, value = line.split('=')
                    if value.isdigit():
                        value = int(value)
                    elif value.replace('.','').isdigit() and value.count('.') == 1:
                        value = float(value)
                    data[key] = value
            return data
        return self.__create_default()

    def __write_file(self):
        if self.data:
            with open(self.path, 'w') as f:
                for key, value in self.data.items():
                    f.write('%s=%s\n' % (key, value))

    def __create_default(self):
        d = dict(app='',
                 value=0,
                 path='')
        return d

    def setValue(self, key, value):
        self.data[key] = value
        self.__write_file()

    def getValue(self, key, default=None):
        return self.data.get(key, default)

    def getSettings(self):
        return self.data

s = settings('c:/mySettings.ini')
s.setValue('app', 'Maya')
