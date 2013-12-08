import sys
from Environment import *
from Lexeme import *
from treeviz import TreeViz

def prettyprint(pt):
    t = TreeViz("out", pt)
    t.viz()
    t.create_image()

def main():
    print("Creating a new Environment")
    glob = create()
    env = extend(None, None, glob)
    print("The environment is: ENV1")
    print("Adding variable x with value 3")
    insert("x",3, env)

    print("Extending the environment with y:4 and z:'hello'")
    print("The environment is ENV2")
    variables = cons("VARIABLE", "y", None)
    variables = cons("VARIABLE", "z", variables)
    values = cons("VALUE", 4, None)
    values = cons("VALUE", "hello", values)
    env2 = extend(variables, values, env)
    print("Looking up value of y (should be 4): ")
    print(lookup("y", env2))
    print("Looking up value x (should be 3): ")
    print(lookup("x", env2))
    
    print("setting value of x to 7")
    update("x", 7, env2)
    print("Checking the new value of x(should be 7): ")
    print(lookup("x", env2))

    print("inserting r with value 5")
    insert("r", 5, env2)
    print("Checking the new value of r(should be 5): ")
    print(lookup("r", env2))
    
    print("Switching to environment ENV1")
    print("Checking the variable 'x' (should be 7): ")
    print(lookup("x", env))

main()
