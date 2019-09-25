import math
import random
def func(n = 5, a= -7, b = 7):
    arr = []
    for i in range(n):
        c = random.randint(a, b)
        arr.append(c)
    return arr
arr = func()
a = 0
for i in arr:
    if i < 0:
        a = math.sqrt(a + i**2)
print(arr)
print(a)


