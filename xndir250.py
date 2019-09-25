import random
def func(n = 5, a = -7, b = 7):
    arr = []
    for i in range(n):
        c = random.randint(a, b)
        arr.append(c)
    return arr
arr = func()
d = 1
for i in range(len(arr)):
    if (arr[i] * i) % 3 == 2:
        d = d * i**2
print(arr)
print(d)


