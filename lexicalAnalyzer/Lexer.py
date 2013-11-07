from Lexeme import *
from Scanner import *

class Lexer:
    def __init__(self, filename):
        self.f = Scanner(filename)
    
    def lex(self):
        if self.f.c == '[':
            return Lexeme("OBRACKET")
        elif self.f.c == ']':
            return Lexeme("CBRACKET")
        elif self.f.c == '.':
            return Lexeme("PERIOD")
        elif self.f.c == ';':
            return Lexeme("SEMICOLON")
        elif self.f.c == ':':
            return Lexeme("COLON")
        elif self.f.c == ',':
            return Lexeme("COMMA")
        elif self.f.c == '+':
            return Lexeme("PLUS")
        elif self.f.c == '-':
            return Lexeme("SUBTRACT")
        elif self.f.c == '*':
            return Lexeme("TIMES")
        elif self.f.c == '/':
            return Lexeme("DIVIDE")
        elif self.f.c == '%':
            return Lexeme("MODULUS")
