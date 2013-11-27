.PHONY: all test scanner

all:

test: scanner

scanner:
	python3 lexicalAnalyzer/Lexer.py program.txt
