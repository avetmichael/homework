import random
def func(n = 6, a = -8, b = 8):
    arr = []
    for i in range(n):
        c = random.randint(a, b)
        arr.append(c)
    return arr
arr = func()
c = 0
for i in arr:
    if i == 0:
        c = c + 1
print(arr)
print(c)
