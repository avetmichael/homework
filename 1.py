arr = [[1, 2], [8, 9]]
b = 1
for i in range(len(arr)):
    for j in range(len(arr[i])):
        b = b * arr[i][j]
        print(arr[i][j], end=' ')
    print()
print(b)
