import random
def func(n = 7, a = -10, b = 10):
    arr = []
    for i in range(n):
       c = random.randint(a, b)
       arr.append(c)
    return arr
arr = func()
v = 0
for i in arr:
    if i != 0:
        v = v + 1
print(arr)
print(v)
