class Lexeme:
    def __init__(self, name):
        self.name = name
        self.value = None
        self.left = None
        self.right = None

    def __str__(self):
        st = "\n"
        if self.name != None:
            st += "\tname: " + self.name + "\n"
        if self.value != None:
            st += "\tvalue: " + str(self.value) + "\n"
        return st

def car(parent):
    if(parent == None):
        return None
    return parent.left

def cdr(parent):
    if(parent == None):
        return None
    return parent.right

def setCar(parent, value):
    if(parent == None):
        return
    parent.left = value

def setCdr(parent, value):
    if(parent == None):
        return
    parent.right = value

def cons(name, left, right):
    parent = Lexeme(name)
    setCar(parent, left)
    setCdr(parent, right)
    return parent
