from Lexeme import Lexeme
from Scanner import Scanner

class Lexer:
    def __init__(self, filename):
        self.f = Scanner(filename)
    
    def lex(self):
        ch = self.f.fgetc()
        self.f.skipWhiteSpace()
        ch = self.f.fgetc()
        if ch == "":
            self.f.close()
            return Lexeme("ENDOFFILE")
            
        if ch == '[':
            return Lexeme("OBRACKET")
        elif ch == ']':
            return Lexeme("CBRACKET")
        elif ch == '.':
            return Lexeme("PERIOD")
        elif ch == ';':
            return Lexeme("SEMICOLON")
        elif ch == ':':
            return Lexeme("COLON")
        elif ch == ',':
            return Lexeme("COMMA")
        elif ch == '+':
            return Lexeme("PLUS")
        elif ch == '-':
            return Lexeme("SUBTRACT")
        elif ch == '*':
            return Lexeme("TIMES")
        elif ch == '/':
            return Lexeme("DIVIDE")
        elif ch == '%':
            return Lexeme("MODULUS")
        elif ch == '&':
            return Lexeme("AND")
        elif ch == '|':
            return Lexeme("OR")
        elif ch == '^':
            return Lexeme("XOR")
        elif ch == '=':
            ch = self.f.fgetc()
            if ch == '=':
                return Lexeme("EQUALS")
            else:
                self.f.ungetc()
                return Lexeme("ASSIGN")
        elif ch == '!':
            ch = self.f.fgetc()
            if ch == '=':
                return Lexeme("NOTEQUALS")
            else:
                self.f.ungetc()
                return Lexeme("NOT")
        elif ch == '<':
            ch = self.f.fgetc()
            if ch == '=':
                return Lexeme("LESSOREQUAL")
            else:
                self.f.ungetc()
                return Lexeme("LESSTHAN")
        elif ch == '>':
            ch = self.f.fgetc()
            if ch == '=':
                return Lexeme("GREATEROREQUAL")
            else:
                self.f.ungetc()
                return Lexeme("GREATERTHAN")
        else:
            if(ch.isdigit()):
                self.f.ungetc()
                return self.lexNumber()
            elif(ch.isalpha()):
                self.f.ungetc()
                return self.lexVariable()
            elif(ch == '"'):
                return self.lexString()
        return self.lexUnknown()

    def lexNumber(self):
        curr = Lexeme("NUMBER")
        num = ""
        ch = self.f.fgetc()
        while(ch.isdigit()):
            num += ch
            ch = self.f.fgetc()
        self.f.ungetc()
        curr.value = int(num)
        return curr

    def lexVariable(self):
        name = ""
        ch = self.f.fgetc()
        while(ch.isalnum()):
            name += ch
            ch = self.f.fgetc()
        if(name == "moenus"):
            curr = Lexeme("FUNCTION")
        elif(name == "dum"):
            curr = Lexeme("WHILE")
        elif(name == "si"):
            curr = Lexeme("IF")
        elif(name == "aut"):
            curr = Lexeme("ELSE")
        elif(name == "revenire"):
            curr = Lexeme("RETURN")
        else:
            curr = Lexeme("VARIABLE")
        curr.value = name
        self.f.ungetc()
        return curr

    def lexString(self):
        curr = Lexeme("STRING")
        string = ""
        ch = self.f.fgetc()
        while(ch != '"'):
            string += ch
            ch = self.f.fgetc()
        curr.value = string
        return curr

    def lexUnknown(self):
        curr = Lexeme("UNKNOWN")
        ch = self.f.fgetc()
        val = ""
        while not ch.isspace():
            val += ch
            ch = self.f.fgetc()
        curr.value = val
        return curr
