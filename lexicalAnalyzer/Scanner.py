class Scanner:
    def __init__(self, filename):
        self.f = open(filename)

    def _nextChar(self):
        return self.c = self.f.read(1)

    def ignoreWhiteSpace(self):
        while(self.c.isspace() or self.c == '#'):
            if(self.c == '#'):
                while(self.c != ';'):
                    self._nextChar()
            self._nextChar()
