import matplotlib.pyplot as plt 
import numpy as np 
import sympy as sy 


def integrate(f, a, b, n=10000000):
    x = np.linspace(a, b, n)
    width = (b-a)/n 
    heights = [f(a)]
    for i in range(n):
        next = f(i*width)
        heights.append(next)
    areas = [i*width for i in heights]
    total_area = sum(areas)
    print('The area under the curve \nis equal to', round(total_area, 2))
    plt.plot(x, f(x))
    plt.fill_between(x, f(x), alpha = 0.3, color = 'blue', hatch = '|')
    plt.title('Sorry this took so Long!')