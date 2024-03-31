class WAV:
    def __init__(self, filename):
        self.filename = filename
        self.data = None
        self.read()
    def read(self):
        with open(self.filename, 'rb') as f:
            self.data = f.read()
    def play(self):
        pass
    def save(self, filename):
        with open(filename, 'wb') as f:
            f.write(self.data)