from sympy import *

L_0 = [0,10]
x= symbols('x')
f = (2*x**2 - 12*x)
delta = 100
l = 1
k = -1
F = [0, 0]

Yk = (L_0[0] + 0.38196*(L_0[1] - L_0[0]))
Zk = (L_0[0] + L_0[1] - Yk)

while delta > l:
    k += 1 
    F[0] = f.subs(x, Yk)
    F[1] = f.subs(x, Zk)

    if F[0] <= F[1]:
        L_0[1] = Zk
        Zk = Yk
        Yk = L_0[0] + L_0[1] - Yk
    else:
        L_0[0] = Yk
        Yk = Zk
        Zk = L_0[0] + L_0[1] - Zk

    delta = abs(L_0[0] - L_0[1])

print(format(((L_0[0] + L_0[1])/2), '.2f'))