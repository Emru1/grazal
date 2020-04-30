import datetime


class Logs:
    def __init__(self, path=''):
        if path == '':
            path = 'log.txt'
        self.file = open(path, 'at')

    def __del__(self):
        self.file.close()

    def log(self, message, sev=0):
        towrite = str(datetime.datetime.now())
        towrite += ' : '
        towrite += message
        towrite += '\n'
        self.file.write(towrite)
