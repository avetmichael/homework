arr = ["a", "b", "c", "d", "e", "f", "g"]
arr2 = []
for i in range(len(arr)):
    if i % 2 == 1:
        arr2.append(arr[i])
print(arr2)
        