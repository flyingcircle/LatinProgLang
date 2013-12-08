import sys
from Lexer import Lexer

def main():
    testFile = sys.argv[1]
    lexer = Lexer(testFile)
    token = lexer.lex()

    while token.name != "ENDOFFILE":
        print(token.name, " ", token.value)
        token = lexer.lex()
    print(token.name)

main()
