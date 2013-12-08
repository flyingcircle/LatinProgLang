import sys
from Lexeme import *

def create():
    return extend(None, None, None)

def extend(variables, values, env):
    return cons("ENV", cons("VALUES", variables, values), env)

def insert(variable, value, env):
    table = car(env)
    setCar(table, cons("VARIABLE", variable, car(table)))
    setCdr(table, cons("VALUE", value, cdr(table)))
    return value

def lookup(variable, env):
    while env != None:
        table = car(env)
        variables = car(table)
        values = cdr(table)
        while variables != None:
            if variable == car(variables):
                return car(values)
            variables = cdr(variables)
            values = cdr(values)
        env = cdr(env)
    print("Found variable that does not exist: ", variable)
    sys.exit(0)
    return None

def update(variable, value, env):
    currEnv = env
    while currEnv != None:
        table = car(currEnv)
        variables = car(table)
        values = cdr(table)
        while variables != None:
            if variable == car(variables):
                setCar(values, value)
                return
            variables = cdr(variables)
            values = cdr(values)
        currEnv = cdr(currEnv)
    insert(variable, value, env)

def printTable(var, val):
    while var != None:
        print(car(var), ":", car(val))
        var = cdr(var)
        val = cdr(val)
    print("No More vars in this env")
