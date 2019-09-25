import random
def func(n = 10, a = -10, b = 10):
    X = []
    for i in range(n):
        X.append(random.randint(a, b))
    return X
X = func()
Y = []
for i in range(len(X)):
    if i % 2 == 1:
        Y.append(X[i])
print(X)
print(Y)