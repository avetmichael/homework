import random
def func(n = 7, a = -19, b = 19):
    X = []
    for i in range(n):
        X.append(random.randint(a, b))
    return X
X = func()
Y = []
for i in X:
    if i % 6 == 1:
        Y.append(i)
print(X)
print(Y)