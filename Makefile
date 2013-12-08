.PHONY: all test array dictionary conditional recursion iteration functions list

all:

test:
	./lat testFiles/sample.lat

run: array dictionary conditional recursion iteration functions list

array:
	cat testFiles/array.lat
	./lat testFiles/array.lat

dictionary:
	cat testFiles/dictionary.lat
	./lat testFiles/dictionary.lat

conditional:
	cat testFiles/conditional.lat
	./lat testFiles/conditional.lat

recursion:
	cat testFiles/recursion.lat
	./lat testFiles/recursion.lat

iteration:
	cat testFiles/iteration.lat
	./lat testFiles/iteration.lat

functions:
	cat testFiles/functions.lat
	./lat testFiles/functions.lat

list:
	cat proglan.lists
	./lat proglan.lists
