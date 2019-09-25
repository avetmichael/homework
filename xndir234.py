import random
def func(n = 8, a = -11, b = 11):
    arr = []
    for i in range(n):
        c = random.randint(a, b)
        arr.append(c)
    return arr
arr = func()
d = 0
e = 0
for i in arr:
    if i < 0:
        d = d + i
        e = e + 1
print(arr)
print(d / e)