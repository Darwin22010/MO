import matplotlib.pyplot as plt
import numpy as np
from sympy import *

L_0 = [0, 10]
x = symbols('x')
f = (2*x**2 - 12*x)
L = 100
E = 0.2
l = 1
k = -1
F = [0, 0]
while L > l:
    k += 1 
    Yk = (L_0[0] + L_0[1] - E)/2
    Zk = (L_0[0] + L_0[1] + E)/2
    F[0] = f.subs(x, Yk)
    F[1] = f.subs(x, Zk)

    if F[0] <= F[1]:
        L_0[1] = Zk
    else:
        L_0[0] = Yk

    L = abs(L_0[1] - L_0[0])

# Функция для преобразования символической функции в функцию NumPy
f_np = lambdify(x, f, modules=['numpy'])

def plot_function(f, start, end, num_points=1000):
    x_vals = np.linspace(start, end, num_points)
    y_vals = f(x_vals)
    plt.plot(x_vals, y_vals)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graph of the Function')
    plt.grid(True)
    plt.show()

plot_function(f_np, L_0[0], L_0[1])
print('Левая грань:')
print(format(L_0[0], '.2f'))
print('Правая грань:')
print(format(L_0[1], '.2f'))
print('Экстремум:')
print(format(((L_0[0] + L_0[1])/2), '.0f'))
