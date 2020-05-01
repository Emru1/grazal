import datetime


class Logs:
    def __init__(self, path=''):
        if path == '':
            path = 'log.txt'
        self.file = open(path, 'at')
        begin = str(datetime.datetime.now()) + ' : Program starts\n'
        self.file.write(begin)

    def __del__(self):
        self.file.write(str(datetime.datetime.now()) + ' : Program ends\n\n\n')
        self.file.close()

    def log(self, message, sev=0):
        towrite = str(datetime.datetime.now())
        towrite += ' : '
        towrite += message
        towrite += '\n'
        self.file.write(towrite)
