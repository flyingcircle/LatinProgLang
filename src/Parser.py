import sys
from Lexer import Lexer
from Lexeme import *

class Parser:
    def __init__(self, filename):
        self.lexer = Lexer(filename)
        self.advance()

    def check(self, name):
        return (self.currLexeme.name == name)

    def advance(self):
        self.currLexeme = self.lexer.lex()

    def matchNoAdvance(self, name):
        if not self.check(name):
            print("illegal")
            print("expected ", name, ", but encountered ", self.currLexeme.name, self.currLexeme.value)
            exit(0)

    def match(self, name):
        self.matchNoAdvance(name)
        temp = self.currLexeme
        if self.currLexeme.name != "ENDOFFILE":
            self.advance()
        return temp

    def operator(self):
        if self.check("PLUS"):
            return self.match("PLUS")
        elif self.check("TIMES"):
            return self.match("TIMES")
        elif self.check("DIVIDE"):
            return self.match("DIVIDE")
        elif self.check("SUBTRACT"):
            return self.match("SUBTRACT")
        elif self.check("MODULUS"):
            return self.match("MODULUS")
        elif self.check("AND"):
            return self.match("AND")
        elif self.check("OR"):
            return self.match("OR")
        elif self.check("XOR"):
            return self.match("XOR")
        elif self.check("EQUALS"):
            return self.match("EQUALS")
        elif self.check("NOTEQUALS"):
            return self.match("NOTEQUALS")
        elif self.check("GREATERTHAN"):
            return self.match("GREATERTHAN")
        elif self.check("LESSTHAN"):
            return self.match("LESSTHAN")
        elif self.check("GREATERTHAN"):
            return self.match("GREATERTHAN")
        elif self.check("GREATEROREQUAL"):
            return self.match("GREATEROREQUAL")
        elif self.check("LESSOREQUAL"):
            return self.match("LESSOREQUAL")

    def operatorPending(self):
        return (self.check("PLUS") or
               self.check("TIMES") or
               self.check("DIVIDE") or
               self.check("SUBTRACT") or
               self.check("MODULUS") or
               self.check("AND") or
               self.check("OR") or
               self.check("XOR") or
               self.check("EQUALS") or
               self.check("NOTEQUALS") or
               self.check("GREATERTHAN") or
               self.check("LESSTHAN") or
               self.check("GREATEROREQUAL") or
               self.check("LESSOREQUAL"))

    def primary(self):
        if self.check("NUMBER"):
            return self.match("NUMBER")
        elif self.check("STRING"):
            return self.match("STRING")
        elif self.check("OBRACKET"):
            self.match("OBRACKET")
            e = self.expression()
            self.match("CBRACKET")
            return e
        elif self.arrayPending():
            return self.array()
        else:
            return self.varExpression()

    def primaryPending(self):
        return (self.check("NUMBER") or
                self.check("STRING") or
                self.varExpressionPending() or
                self.check("OBRACKET"))

    def varExpression(self):
        v = self.match("VARIABLE")
        if self.check("OBRACKET"):
            self.match("OBRACKET")
            l = self.optList()
            self.match("CBRACKET")
            return cons("FUNCTION_CALL", v, l)
        return v

    def varExpressionPending(self):
        return self.check("VARIABLE")

    def expression(self):
        p = self.primary()
        if self.operatorPending():
            o = self.operator()
            e = self.expression()
            return cons("EXPRESSION", p, cons("GLUE", o, e))
        return cons("EXPRESSION", p, None)

    def expressionPending(self):
        return self.primaryPending()

    def list(self):
        e = self.expression()
        if self.check("COMMA"):
            self.match("COMMA")
            return cons("LIST", e, self.list())
        return cons("LIST", e, None)
        
    def optList(self):
        if self.expressionPending():
            return self.list()
        return None
        
    def assignment(self):
        v = self.match("VARIABLE")
        self.match("ASSIGN")
        e = self.expression()
        return cons("ASSIGN", v, e)
        
    def array(self):
        self.match("COLON")
        l = self.optList()
        self.match("SEMICOLON")
        return cons("ARRAY", None, l)
        
    def arrayPending(self):
        return self.check("COLON")
        
    def statement(self):
        if self.ifStatementPending():
            return self.ifStatement()
        elif self.whileStatementPending():
            return self.whileStatement()
        elif self.functionDefPending():
            return self.functionDef()
        elif self.check("RETURN"):
            self.match("RETURN")
            s = self.expression()
            self.match("PERIOD")
            return cons("RETURN", s, None)
        else:
            s = self.match("VARIABLE")
            if self.check("ASSIGN"):
                self.match("ASSIGN")
                s = cons("ASSIGN", s, self.expression())
            else:
                self.match("OBRACKET")
                s = cons("FUNCTION_CALL", s, self.optList())
                self.match("CBRACKET")
            self.match("PERIOD")
            return s

    def statementPending(self):
        return (self.ifStatementPending() or
                self.whileStatementPending() or
                self.functionDefPending() or
                self.check("VARIABLE"))
    
    def block(self):
        if self.check("SEMICOLON"):
            self.match("SEMICOLON")
        else:
            s = self.statement()
            return cons("BLOCK", s, self.block())
        return None

    def ifStatement(self):
        self.match("IF")
        self.match("OBRACKET")
        cond = self.expression()
        self.match("CBRACKET")
        b = self.block()
        e = self.optElse()
        return cons("IF", cond, cons("GLUE", b, e))

    def ifStatementPending(self):
        return self.check("IF")

    def optElse(self):
        if self.check("ELSE"):
            self.match("ELSE")
            b = self.block()
            return cons("ELSE", b, None)
        return None

    def whileStatement(self):
        self.match("WHILE")
        self.match("OBRACKET")
        cond = self.expression()
        self.match("CBRACKET")
        return cons("WHILE", cond, self.block())

    def whileStatementPending(self):
        return self.check("WHILE")

    def args(self):
        param = self.match("VARIABLE")
        if self.check("COMMA"):
            self.match("COMMA")
            return cons("PARAMETERS", param, self.args())
        return cons("PARAMETERS", param, None)

    def optArgs(self):
        if self.check("VARIABLE"):
            return self.args()
        return None

    def functionDef(self):
        self.match("FUNCTION")
        name = self.match("VARIABLE")
        self.match("OBRACKET")
        parameters = self.optArgs()
        self.match("CBRACKET")
        body = self.block()
        return cons("FUNCTION_DEF", name, cons("GLUE", parameters, body))

    def functionDefPending(self):
        return self.check("FUNCTION")

    def program(self):
        s = self.statement()
        if self.programPending():
            return cons("GLOBAL", s, self.program())
        else:
            return cons("GLOBAL", s, self.match("ENDOFFILE"))

    def programPending(self):
        return self.statementPending()
