from Parser import Parser
from Environment import *
from Evaluator import *
from Builtins import *
import sys

def main():
    filename = sys.argv[1]
    if(len(sys.argv) != 2):
        print("Unknown arguments: should only take a single file")
        exit(0)
    parsed = Parser(filename)
    pt = parsed.program()
    env = create()
    addBuiltins(env)
    Eval(pt, env)

main()
