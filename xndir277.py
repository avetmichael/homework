arr = ["a", "b", "c", "d", "e", "f", "g"]
arr2 = []
for i in arr:
    if i == "d":
        arr.remove(i)
        arr2.append(arr)
print(arr2)