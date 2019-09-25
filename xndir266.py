import random
def func1(n = 5, a = -7, b = 7):
    X = []
    for i in range(n):
        c = random.randint(a, b)
        X.append(c)
    return X
Y = func1()
X = func1()
m = 0
for i in X:
    if i % 2 == 1:
        m = m + i
k = 0
for i in Y:
    if i % 2 == 0:
        k = k + i
print(X)
print(Y)
print(m - k)