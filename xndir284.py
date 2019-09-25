import random
def func(n = 7, a = -10, b = 10):
    X = []
    for i in range(n):
        X.append(random.randint(a, b))
    return X
X = func()
Y = func()
print(X)
print(Y)