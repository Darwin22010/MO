import numpy as np

x_0 = np.array([0, 0, 0])
t = 0.5
E1 = 0.05
E2 = 0.001
k_max = 10000

def f(x):
    x1, x2, x3 = x
    return (x1 - 3)**2 + 2*(x2 - 4)**2 + 3*(x3 + 1)**2

def gradient(x):
    x1, x2, x3 = x
    df_dx1 = 2*(x1 - 3)
    df_dx2 = 4*(x2 - 4)
    df_dx3 = 6*(x3 + 1)
    return np.array([df_dx1, df_dx2, df_dx3])

def gradient_descent(gradient, x_0, t, E1, k_max, E2):
    x = x_0
    k = 0
    
    while True:
        grad = gradient(x)
        x_new = x - t * grad
        k += 1
        
        if np.linalg.norm(grad) < E1 or k >= k_max:
            break

        if f(x_new) - f(x) >= 0:
          x, k = gradient_descent(gradient, x, t / 2, E1, k_max, E2)
          break
        
        if abs(np.linalg.norm(x_new) - np.linalg.norm(x)) < E2 and abs(f(x_new) - f(x)) < E2:
          return x, k

        
        x = x_new
    
    return x, k

result, k = gradient_descent(gradient, x_0, t, E1, k_max, E2)

print("Минимум функции:"),
for i in range(len(result)):
    print(format(result[i], '.2f'))
print("Количество иттераций:", k)