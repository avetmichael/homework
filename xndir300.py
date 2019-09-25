import random
def func(n = 5, a = -10, b = 10):
    X = []
    for i in range(n):
        X.append(random.randint(a, b))
    return X
X = func()
Y = []
k = 25
for i in X:
    if i**2 > k:
        Y.append(i)
print(X)
print(Y)