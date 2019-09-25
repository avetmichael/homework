import math
import random
def func(n = 10, a = -20, b = 20):
    arr = []
    for i in range(n):
        c = random.randint(a, b)
        arr.append(c)
    return arr
arr = func()
k = 5
a = 1
for i in arr:
    if math.fabs(i) > k:
        a = a * i
print(arr)
print(a)
