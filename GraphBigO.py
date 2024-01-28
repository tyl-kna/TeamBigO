import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
import re

# Define the symbolic variable
n = sp.symbols("n_a")

# Big O notation passed in as an argument
def PlotBigO(complexity):
    fig = plt.figure()
    plt.figure().clear()
    plt.cla()
    plt.clf()
    plt.figure(figsize=(10, 10))
    for c in complexity:
        string = re.search("[a-zA-Z].*[a-zA-Z]", str(c))
        temp = str(c)[string.start(): string.end()]
        var = sp.symbols(temp)
        # Convert the symbolic expression to a NumPy complexity
        f_np = sp.lambdify(var, c, 'numpy')
        # Generate an array of values for n
        x = np.arange(1, 15)

        plt.plot(x, f_np(x))
    
    plt.xlabel("n", fontsize = 30)
    # Make the exponents superscripted
    parts = re.split(r"\*\*[\d\w]+", str(complexity))
    exponents = re.findall(r"(?<=\*\*)[\d\w]+", str(complexity))
    fixed_exponents = ["$\mathregular{^" + exp + "}$" for exp in exponents]
    temp = parts[0]
    temp += "".join([a+b for a, b in zip(fixed_exponents, parts[1:])])

    plt.ylabel(temp, fontsize = 30)
    #plt.tight_layout() 
    plt.title("O(" + temp + ")", fontsize = 40)
    plt.show() 
    #plt.savefig("plot.jpg")
