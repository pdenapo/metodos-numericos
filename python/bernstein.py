#!/usr/bin/env python3
# Aproximación a una función continua mediante los polinomios de Bernstein
# (prueba del teorema de aproximación de Weierstrass)
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st


# La función a aproximar
def f(x):
    return np.abs(1 / 2 - x)


def bernstein(f, n, p):
    return np.sum(
        [f(k / n) * st.binom.pmf(k, n, p) for k in np.arange(0, n + 1)])


# Create the vectors X and Y
x = np.linspace(0, 1, num=1000)
y = f(x)
# Create the plot
plt.plot(x, y, 'blue', label='f(x)')

bernstein3 = lambda x: bernstein(f, 3, x)
bernstein3 = np.vectorize(bernstein3)
y3 = bernstein3(x)
plt.plot(x, y3, 'green', label='$B_3$')

bernstein10 = lambda x: bernstein(f, 10, x)
bernstein10 = np.vectorize(bernstein10)
y10 = bernstein10(x)
plt.plot(x, y10, 'red', label='$B_{10}$')

bernstein100 = lambda x: bernstein(f, 100, x)
bernstein100 = np.vectorize(bernstein100)
y100 = bernstein100(x)
plt.plot(x, y100, 'magenta', label='$B_{100}$')

bernstein300 = lambda x: bernstein(f, 300, x)
bernstein300 = np.vectorize(bernstein300)
y300 = bernstein300(x)
plt.plot(x, y300, 'brown', label='$B_{300}$')

# Show the plot
plt.legend(loc="upper left")
plt.show()
