class Scanner:
    def __init__(self, filename):
        self.f = open(filename)
        self._stack = list()

    def _nextChar(self):
        self.c = self.f.read(1)

    def skipWhiteSpace(self):
        while(self.c.isspace() or self.c == '#'):
            if(self.c == '#'):
                while(self.c != ';'):
                    self.fgetc()
            self.fgetc()
        self.ungetc()

    def ungetc(self):
        self._stack.append(self.c)
    
    def fgetc(self):
        if(len(self._stack) == 0):
            self._nextChar()
            return self.c
        else:
            self.c = self._stack.pop()
            return self.c

    def close(self):
        self.f.close()
