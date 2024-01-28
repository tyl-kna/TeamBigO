import sympy as sp

def Valid(loopVal):
    start = loopVal[0]
    end = loopVal[1]
    d = loopVal[2]
    if (type(end) != str and type(start) != str):
        if (end - start) * d <= 0:
            return False
    return True

def ForComplexity(loopVal):
    start = loopVal[0]
    end = loopVal[1]
    d = loopVal[2]
    # If the for loop is invalid, complexity is only 1
    # The reason for this is because it does one comparison and fails on the first check
    # Python prevents invalid for loops after checking if it's valid or not
    if (not Valid(loopVal)):
        return sp.simplify("1")
    
    # If the for loop is valid, use equation
    # complexity = ceil(end - start)/step + 1

    # Integer division
    expression = "(" + str(end) + " - " + str(start) + ") " 
    if (type(end) != str and type(start) != str):
        expression = expression + "// " + str(d)
    else:
        expression = expression + "/ " + str(d)
    # Ceiling (dont do this for strings)
    if type(end) != str and type(start) != str and (end - start) % d != 0:
        expression = expression + " + 1"
    return sp.simplify(expression + " + 1")

# Returns the simplified symbolic expression of two symbolic functions being added together
def AddExp(exp1, exp2):
    return sp.simplify(("(" + str(exp1) + ") + (" + str(exp2) + ")"))

# Returns the simplified symbolic expression for multiplication between two symbolic expressions
def MulExp(exp1, exp2):
    return (sp.simplify("(" + str(exp1) + ") * (" + str(exp2) + ")"))

# Returns the simplified symbolic expression for division between two symbolic expressions
def DivExp(exp1, exp2):
    return (sp.simplify("(" + str(exp1) + ") / (" + str(exp2) + ")"))

# Subtracts a value from the symbolic expression
def SubVal(exp1, val):
    return sp.simplify("(" + str(exp1) + ") - (" + str(val) + ")")

# def test():
#     M = [(0, "N_1", 3), (0, "N_2", 3), (0, 10, 0)]

#     arg1 = sp.simplify(ForComplexity(M[0]))
#     arg2 = sp.simplify(ForComplexity(M[1]))
#     print("Original expressions", arg1, arg2, sep="\n")

#     print("Using add function", AddExp(arg1, arg2), sep = "\n")
#     print("Using mul function", MulExp(arg1, arg2), sep = "\n")
#     print("Using div function", DivExp(arg1, arg2), sep = '\n')
#     print("Using sub function on ", arg2, "\n", SubVal(arg2, 1), sep="")

# test()