r = 1
x1 = 0
x2 = -1
f = 0
l1 = 0
for i in range (5):
    x1 = (16 * r - 1)/(3*r)
    f = x1 - 2 * x2**2 - 3 * x2 + 10 + (r/2) * (3*x1+4*x2-12)**2
    l1 = r * (3*x1+4*x2-12)
    print(r)
    print(x1)
    print(f)
    print(l1)
    r *= 10