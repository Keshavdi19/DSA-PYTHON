arr = [1, 2, 3, 4, 5]
res = []
for i in range(len(arr)-1, -1, -1):
    res.append(arr[i])
print(res)