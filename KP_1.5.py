"""""
from sympy import *

x1, x2 = symbols('x1 x2')
z = [1,2]
z[0] = (diff(((x1-3)**2 + 2*(x2-4)**2), x1))
z[1] = (diff(((x1-3)**2 + 2*(x2-4)**2), x2))
z[1].subs(x, 10)
for i in range(len(z)):
    print(z[i])
"""""
from sympy import *
x_0 = [2,3,0]
x_0next = [1.324,12.896,0.984]
grad = [0,0,0]
E_1 = 0.1
E_2 = 0.15
M = 10
B = 0
Ft = 0
d = [2,4,-6]
x1, x2, x3, t = symbols('x1 x2 x3 t')
X = [x1,x2,x3]
f = ((x1-3)**2 + 2*(x2-4)**2 + 3*(x3+1)**2)
k = -1
def step_1():
    for i in range(len(x_0)):
        grad[i] = diff(f, X[i])

def step_2():
    k = k + 1

def step_3(xnow):
    x = xnow
    grad_res = [0,0,0]
    for i in range(len(x_0)):
        grad_res[i] = (grad[i]).subs(X[i], x[i])
    return grad_res

def step_4(xnow):
    grad_res = step_3(xnow)
    norm = 0
    for i in range(len(x_0)):
        norm += grad_res[i]**2
    norm = norm**0.5
    return norm

def step_5():
    if k >= M:
        print(5)

def step_6(xnow):
    d_k = step_3(xnow)
    for i in range(len(x_0)):
        d_k[i] *= -1
    return d_k

def step_7():
    b1 = (step_4(x_0))**2
    b2 = (step_4(x_0next))**2
    B = b2 / b1
    return B

def step_8():
    for i in range(len(x_0)):
        d[i] = step_6(x_0)[i] + B * d[i]
    return d

def step_9():
    for i in range(len(x_0)):
        x_0next[i] = x_0[i] + t*d[i]
    Ft = f
    for i in range(len(x_0)):
        Ft = Ft.subs(X[i], x_0next[i])
    b = solve(diff(Ft, t), t)
    print(b)
    b = 0.194
    p = [0,0,0]
    for i in range(len(x_0)):
        p[i] = x_0next[i].subs(t, b)
    print(p)
    u = 0
    a = [0,0,0]
    for i in range(len(x_0)):
        a[i] = (x_0next[i] - x_0[i])
    for i in range(len(x_0)):
        u = u + a[i]**2
    u = sqrt(u)
    print(u)


def step_10():
    b = 0.194
    p = [0,0,0]
    for i in range(len(x_0)):
        p[i] = x_0next[i].subs(t, b)
    print(p)

def step_11():
    u = 0
    a = [0,0,0]
    for i in range(len(x_0)):
        a[i] = (x_0next[i] - x_0[i])
    for i in range(len(x_0)):
        u = u + a[i]**2
    u = sqrt(u)
    print(u)

step_9()

