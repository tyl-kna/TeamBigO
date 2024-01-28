def testFunction(a: int):
    x = 0
    for i in range(a):
        for j in range(a):
            x += 1
    return x

def testFunction2(x: list):
    z = 0
    for i in range(len(x)):
        z += 1
    return z
