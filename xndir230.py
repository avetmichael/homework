import math
arr = [10.1, 12, 462, 34.2, 52.4, 214]
k = 5
b = 0
for i in arr:
    if int(i) % k == 0:
        b = math.sqrt((b + int(i) ** 2))
print(b)



