from Builtins import *
from Environment import *

def Eval(tree, env):
    if tree == None:
        return
    name = tree.name
    
    if name == "NUMBER":
        return tree.value
    elif name == "STRING":
        return tree.value
    elif name == "ARRAY":
        return evalArray(tree, env)
    elif name == "VARIABLE":
        return lookup(tree.value, env)
    elif name == "ASSIGN":
        return evalAssign(tree, env)
    elif name == "RETURN":
        return evalReturn(tree, env)
    elif name == "EXPRESSION":
        return evalExpression(tree, env)
    elif name == "FUNCTION_DEF":
        return evalFuncDef(tree, env)
    elif name == "IF":
        return evalIf(tree, env)
    elif name == "WHILE":
        return evalWhile(tree, env)
    elif name == "FUNCTION_CALL":
        return evalFuncCall(tree, env)
    elif name == "BLOCK":
        return evalBlock(tree, env)
    elif name == "GLOBAL":
        return evalGlobal(tree, env)
    elif name == "ENDOFFILE":
        return
    else:
        print("bad expression: ", name)
        exit(0)

def evalFuncDef(t, env):
    closure = cons("CLOSURE", t.right, env)
    insert(t.left.value , closure, env)

def evalFuncCall(t, env):
    closure = Eval(t.left, env)
    if closure.name == "BUILTIN":
        return evalBuiltin(closure, t.right, env)
    args = t.right
    params = formatParams(closure.left.left)
    body = closure.left.right
    senv = closure.right
    eargs = evalArgs(args, env)
    xenv = extend(params, eargs, senv)
    return Eval(body, xenv)

def evalBuiltin(closure, args, env):
    argList = list()
    while args != None:
        argList.append(Eval(args.left, env))
        args = args.right
    return closure.left(*argList)

def formatParams(t):
    if t != None:
        return cons("VARIABLE", t.left.value, formatParams(t.right))
    else:
        return None

def evalArgs(t, env):
    if t != None:
        return cons("VALUE", Eval(t.left, env), evalArgs(t.right, env))
    else:
        return None

def evalBlock(t, env):
    result = None
    while t != None:
        if t.name == "RETURN":
            return evalReturn(t, env)
        value = Eval(t.left, env)
        if value != None and t.left.name != "FUNCTION_CALL":
            return value
        t = t.right
    return None

def evalIf(t, env):
    value = None
    if Eval(t.left, env) != 0:
        value = evalBlock(t.right.left, env)
    elif t.right.right != None:
        value = evalBlock(t.right.right, env)
    if value != None:
        return value

def evalWhile(t, env):
    value = None
    while Eval(t.left, env) != 0:
        value = evalBlock(t.right, env)
        if value != None:
            return value

def evalExpression(t, env):
    if t.right != None:
        return evalSimpleOp( cons(t.right.left.name, t.left, t.right.right), env)
    else:
        return Eval(t.left, env)

def evalSimpleOp(t, env):
    if t.name == "PLUS":
        return evalPlus(t, env)
    elif t.name == "SUBTRACT":
        return evalSubtract(t, env)
    elif t.name == "TIMES":
        return evalTimes(t, env)
    elif t.name == "DIVIDE":
        return evalDivide(t, env)
    elif t.name == "MODULUS":
        return evalModulus(t, env)
    elif t.name == "AND":
        return evalAnd(t, env)
    elif t.name == "OR":
        return evalOr(t, env)
    elif t.name == "XOR":
        return evalXor(t, env)
    elif t.name == "EQUALS":
        return evalEquals(t, env)
    elif t.name == "NOTEQUALS":
        return evalNotEquals(t, env)
    elif t.name == "GREATERTHAN":
        return evalGreaterThan(t, env)
    elif t.name == "LESSTHAN":
        return evalLessThan(t, env)
    elif t.name == "GREATEROREQUAL":
        return evalGreaterOrEqual(t, env)
    elif t.name == "LESSOREQUAL":
        return evalLessOrEqual(t, env)

def evalPlus(t, env):
    left = Eval(t.left, env)
    right = Eval(t.right, env)
    value = left + right
    return value

def evalSubtract(t, env):
    left = Eval(t.left, env)
    right = Eval(t.right, env)
    value = left - right
    return value

def evalTimes(t, env):
    left = Eval(t.left, env)
    right = Eval(t.right, env)
    value = left * right
    return value

def evalDivide(t, env):
    left = Eval(t.left, env)
    right = Eval(t.right, env)
    value = left / right
    return value

def evalModulus(t, env):
    left = Eval(t.left, env)
    right = Eval(t.right, env)
    value = left % right
    return value

def evalAnd(t, env):
    left = Eval(t.left, env)
    if left == 0: #0 being false and all other numbers true
        value = 0
    else:
        right = Eval(t.right, env)
        if right == 0:
            value = 0
        else:
            value = 1
    return value

def evalOr(t, env):
    left = Eval(t.left, env)
    if left != 0:
        value = 1
    else:
        right = Eval(t.right, env)
        if right != 0:
            value = 1
        else:
            value = 0
    return value

def evalXor(t, env):
    left = Eval(t.left, env)
    right = Eval(t.right, env)
    if (left != 0 and right != 0) or (left == 0 and right == 0):
        value = 0
    else:
        value = 1
    return value

def evalEquals(t, env):
    left = Eval(t.left, env)
    right = Eval(t.right, env)
    if left == right:
        value = 1
    else:
        value = 0
    return value

def evalNotEquals(t, env):
    left = Eval(t.left, env)
    right = Eval(t.right, env)
    if left != right:
        value = 1
    else:
        value = 0
    return value

def evalLessThan(t, env):
    left = Eval(t.left, env)
    right = Eval(t.right, env)
    if left < right:
        value = 1
    else:
        value = 0
    return value
    
def evalGreaterThan(t, env):
    left = Eval(t.left, env)
    right = Eval(t.right, env)
    if left > right:
        value = 1
    else:
        value = 0
    return value

def evalGreaterOrEqual(t, env):
    left = Eval(t.left, env)
    right = Eval(t.right, env)
    if left >= right:
        value = 1
    else:
        value = 0
    return value

def evalLessOrEqual(t, env):
    left = Eval(t.left, env)
    right = Eval(t.right, env)
    if left <= right:
        value = 1
    else:
        value = 0
    return value

def evalReturn(t, env):
    return Eval(t.left, env) 

def evalAssign(t, env):
    value = Eval(t.right, env)
    update(t.left.value, value, env)

def evalList(t, env):
    curr = t
    l = list()
    while t != None:
        l.append(Eval(t.left, env))
        t = t.right
    return l

def evalArray(t, env):
    return evalList(t.right, env)

def evalGlobal(t, env):
    Eval(t.left, env)
    Eval(t.right, env)
