class Maps:
    def __init__(self):
        self.maps = {}

    def add(self, name, mmap):
        self.maps[name] = mmap

    def get(self, name):
        return self.maps[name]
