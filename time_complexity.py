import pathlib 
import os 
import sys
from sympyVisit import *
def main():
    if len(sys.argv) != 2: 
        print("Error: Invalid number of args")
        exit(1)
    
    try:
        file_name = sys.argv[1]
        file = open(file_name, "r")
    except Exception as e: 
        print("There has been an error: %s" % (e))
        exit(1)

    #for line in file: 
    #    print(line)
    #print(sys.argv[1])
    tree = ast.parse(file.read())
    visitor = Visitor(file_name)
    visitor.visit(tree)
    visitor.compute_statistics()
main()
