import random
def func(n = 10, a = - 35, b = 35):
    X = []
    for i in range(n):
        X.append(random.randint(a, b))
    return X
X = func()
Y = func()
k = 0
for i in X:
    if i % 7 == 0:
        k = k + i
m = 0
for i in Y:
    if i % 7 == 0:
        m = m + i
print(X)
print(Y)
print(k + m)

