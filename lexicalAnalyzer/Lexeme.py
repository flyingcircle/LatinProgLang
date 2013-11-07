class Lexeme:
    def __init__(self, name):
        self.name = name
        self.value = None
        self._left = None
        self._right = None

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self._left = None
        self._right = None

    def car(self):
        return self._left

    def cdr(self):
        return self._right

    def setCar(self, value):
        self._left = value

    def setCdr(self, value):
        self._right = value

def cons(name, left, right):
    parent = Lexeme(name)
    parent.setCar(left)
    parent.setCdr(right)
