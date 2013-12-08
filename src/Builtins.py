from Environment import *

def __lookupArray__(arr, ind):
    return arr[ind]

def __createArray__(n):
    return [None] * n

def __setIndex__(arr, ind, val):
    arr[ind] = val

def __createDict__():
    return dict()

def __insertDict__(dic, key, val):
    dic[key] = val

def __getValDict__(dic, key):
    return dic[key]

def __negate__(val):
    return -val

def __toString__(val):
    return str(val)

def addBuiltins(env):
    insert("legere", cons("BUILTIN", print, None), env)
    insert("potiorIndicina", cons("BUILTIN", __lookupArray__, None), env)
    insert("creareAcies", cons("BUILTIN", __createArray__, None), env)
    insert("locareIndicina", cons("BUILTIN", __setIndex__, None), env)
    insert("creareLexicon", cons("BUILTIN", __createDict__, None), env)
    insert("indereLexicon", cons("BUILTIN", __insertDict__, None), env)
    insert("pervidereLexicon", cons("BUILTIN", __getValDict__, None), env)
    insert("neg", cons("BUILTIN", __negate__, None), env)
    insert("facereStrictus", cons("BUILTIN", __toString__, None), env)
