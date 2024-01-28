import sympy as sp

def Valid(loopVal):
    start = loopVal[0]
    end = loopVal[1]
    d = loopVal[2]
    if (end - start) * d <= 0:
        return False
    return True

def ForComplexity(loopVal):
    start = loopVal[0]
    end = loopVal[1]
    d = loopVal[2]

    # Integer division
    expression = "(" + str(end) + " - " + str(start) + ") " 
    if (type(end) != str and type(start) != str):
        expression = expression + "// " + str(d)
    else:
        expression = expression + "/ " + str(d)
    # Ceiling (dont do this for strings)
    if type(end) != str and type(start) != str and (end - start) % d != 0:
        expression = expression + " + 1"
    return (expression + " + 1")

def test():
    M = [(0, "N_1", 1), (0, "N_2", 2), (0, 10, 3)]
    for i in range(len(M)):
        print(sp.simplify(ForComplexity(M[i])))


    


    '''
    for i in range(N, 0, 1):        # worst case: (0 - N ) / 1 + 1 - > -N + 1    assume N < 0
        for j in range(N, 0, -1):   #  Has to be (1) * (N)  (0 - n) / -1 - > -n/-1 -> n
            print()                 # This won't run
                                    # Total = N + 1 + N ---> 2N + 1
    '''


test()