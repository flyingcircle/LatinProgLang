import sys
from Parser import Parser
from treeviz import TreeViz

def prettyPrint(pt):
    t = TreeViz("out", pt)
    t.viz()
    t.create_image()
    t.open_image()

def main():
    filename = sys.argv[1]
    graphFlag = False
    if(len(sys.argv) == 3 and sys.argv[2] == "--graph"):
        graphFlag = True
    p = Parser(filename)
    pt = p.program()
    if graphFlag:
        prettyPrint(pt)
    print("legal")

main()
