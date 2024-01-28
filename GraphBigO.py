import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
import re

# Define the symbolic variable
n = sp.symbols("n")

# Big O notation passed in as an argument
def PlotBigO(complexity):
    # Convert the symbolic expression to a NumPy complexity
    f_np = sp.lambdify(n, complexity, 'numpy')

    # Generate an array of values for n
    x = np.arange(1, 1000)

    plt.figure(figsize=(10, 10))
    plt.plot(x, f_np(x))
    plt.xlabel("n", fontsize = 30)
    
    # Make the exponents superscripted
    parts = re.split(r"\*\*[\d\w]+", str(complexity))
    exponents = re.findall(r"(?<=\*\*)[\d\w]+", str(complexity))
    fixed_exponents = ["$\mathregular{^" + exp + "}$" for exp in exponents]
    temp = parts[0]
    temp += "".join([a+b for a, b in zip(fixed_exponents, parts[1:])])

    plt.title("O(" + temp + ")", fontsize = 40)
    plt.ylabel(temp, fontsize = 30)

    plt.tight_layout() 

    plt.savefig("plot.jpg")
