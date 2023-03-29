"""""
from sympy import *
x_0 = [2,3,0]
x_0next = [2,1,0]
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


    n = 0
    for i in range(len(x_0)):
        n = f.subs([(x1, x_0next[0]), (x2, x_0next[1]), (x3, x_0next[2])])
        m = f.subs([(x1, x_0[0]), (x2, x_0[1]), (x3, x_0[2])])
    print(abs(n-m))
"""""
from sympy import *
n11 = 100
n12 = 100
x_0 = [2,3,0]
x_0next = [2,1,0]
grad = [0,0,0]
d = [0,0,0]
E_1 = 0.9
E_2 = 0.99
M = 10
x1, x2, x3, t = symbols('x1 x2 x3 t')
X = [x1,x2,x3]
f = ((x1-3)**2 + 2*(x2-4)**2 + 3*(x3+1)**2)
k = -1
while n11 > E_2 or n12 > E_2:
#1-2
    k += 1
    for i in range(len(x_0)):
        grad[i] = diff(f, X[i])
#3
    grad_res = [0,0,0]
    for i in range(len(x_0)):
        grad_res[i] = (grad[i]).subs(X[i], x_0[i])

    norm = 0
    for i in range(len(x_0)):
        norm += grad_res[i]**2
    norm = norm**0.5
#4
    if norm < E_1:
        print('Вышли на 4 шаге')
        for i in range(len(x_0)):
            print(format(x_0next[i], '.2f'))
        quit()
#5
    if k >= M:
        print('Вышли на 5 шаге')
        for i in range(len(x_0)):
            print(format(x_0next[i], '.2f'))
        quit()
#6
    elif k == 0:
        for i in range(len(x_0)):
            d[i] = grad_res[i] * -1
        #9
        for i in range(len(x_0)):
            x_0next[i] = x_0[i] + t*d[i]

        Ft = f.subs([(x1, x_0next[0]), (x2, x_0next[1]), (x3, x_0next[2])])
        t_res = solve(diff(Ft, t), t)
        t_res = Float(t_res[0])
#7
    else:
        grad_res = [0,0,0]
        for i in range(len(x_0)):
            grad_res[i] = (grad[i]).subs(X[i], x_0next[i])
        norm1 = 0
        for i in range(len(x_0)):
            norm1 += grad_res[i]**2

        grad_res1 = [0,0,0]
        for i in range(len(x_0)):
            grad_res1[i] = (grad[i]).subs(X[i], x_0[i])
        norm2 = 0
        for i in range(len(x_0)):
            norm2 += grad_res[i]**2

        B = norm1/norm2
#8      
        for i in range(len(x_0)):
            d[i] = -grad_res[i] + B * d[i]

#9      
        for i in range(len(x_0)):
            x_0next[i] = x_0[i] + t*d[i]

        Ft = f.subs([(x1, x_0next[0]), (x2, x_0next[1]), (x3, x_0next[2])])
        t_res = solve(diff(Ft, t), t)
        t_res = Float(t_res[0])
#10
    for i in range(len(x_0)):
        x_0next[i] = x_0[i] + t_res * d[i]

#11
    u = 0
    a = [0,0,0]
    for i in range(len(x_0)):
        a[i] = (x_0next[i] - x_0[i])
    for i in range(len(x_0)):
        u = u + a[i]**2
    n11 = sqrt(u)

    n = f.subs([(x1, x_0next[0]), (x2, x_0next[1]), (x3, x_0next[2])])
    m = f.subs([(x1, x_0[0]), (x2, x_0[1]), (x3, x_0[2])])
    n12 = abs(n-m)

print(k)
print('Вышли на 11 шаге')
for i in range(len(x_0)):
    print(format(x_0next[i], '.2f'))
