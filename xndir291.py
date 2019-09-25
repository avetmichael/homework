import random
def func(n = 8, a = -13, b = 13):
    X = []
    for i in range(n):
        X.append(random.randint(a, b))
    return X
X = func()
Y = []
print(X)
for i in X:
    if i < 0:
        Y.append(i)
print(Y)

