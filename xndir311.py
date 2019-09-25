import random
def func(n = 7, a = -20, b = 20):
    X = []
    for i in range(n):
        X.append(random.randint(a, b))
    return X
X = func()
Y = []
for i in X:
    if i > 0:
        Y.append(i + max(X))
print(X)
print(Y)
#maxov vor areci miavor talu es?)))

