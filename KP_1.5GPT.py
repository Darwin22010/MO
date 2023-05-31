from scipy.optimize import minimize
from sympy import diff, symbols

# Определение переменных
x1, x2, x3 = symbols('x1 x2 x3')
X = [x1, x2, x3]

# Задание функции
f = (x1 - 3)**2 + 2*(x2 - 4)**2 + 3*(x3 + 1)**2

# Градиент функции
grad = [diff(f, X[i]) for i in range(len(X))]

# Функция для оптимизации
def objective(x):
    return f.subs([(X[i], x[i]) for i in range(len(X))])

# Начальная точка
x0 = [0, 0, 0]

# Минимизация функции
res = minimize(objective, x0, jac=[grad[i] for i in range(len(X))], method='CG')

# Вывод результатов
print(f'Минимум функции: {res.fun}')
print(f'Количество итераций: {res.nit}')
print(f'Конечная точка: {res.x}')
