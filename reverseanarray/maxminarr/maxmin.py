arr = [20, 50, 10, 90, 30]
mx = arr[0]
mn = arr[0]
for num in arr:
    if num > mx:
        mx = num
    if num < mn:
        mn = num
print(mx, mn)
