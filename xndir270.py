import random
def func(n = 5, a = -5, b = 5):
    X = []
    for i in range(n):
        X.append(random.randint(a, b))
    return X
X = func()
Y = func()
k = 0
for i in X:
    k = k + i**2
m = 0
for i in Y:
    m = m + i**2
print(X)
print(Y)
print(k + m)