from sympy import *

L_0 = [0,10]
x= symbols('x')
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

print(format(((L_0[0] + L_0[1])/2), '.2f'))