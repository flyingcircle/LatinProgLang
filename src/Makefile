.PHONY: all clean test run scanner recognizer environment lat

all:

test: run

run: environment

scanner:
	python3 testLex.py ./testFiles/program.txt

recognizer:
	python3 testParser.py ./testFiles/program.txt
	python3 testParser.py ./testFiles/MissingPeriod.txt
	python3 testParser.py ./testFiles/nestedFunctionCall.txt
	python3 testParser.py ./testFiles/noEndingBlock.txt

environment:
	python3 testEnvironment.py

lat:
	./lat ./testFiles/sample.lat

clean:
	@- $(RM) *~
	@- $(RM) -r __pycache__
	@- $(RM) out.dot out.png
