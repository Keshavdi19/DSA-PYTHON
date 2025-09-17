arr = [5, 7, 2, 9, 1]

# Step 1: assume first element sabse bada
max1 = arr[0]
max2 = float('-inf')   # sabse chhota number

# Step 2: traverse array
for i in range(1, len(arr)):
    if arr[i] > max1:
        max2 = max1
        max1 = arr[i]
    elif arr[i] > max2 and arr[i] != max1:
        max2 = arr[i]

# Step 3: print
if max2 == float('-inf'):
    print("No second maximum (sab elements same hain)")
else:
    print("Second Maximum:", max2)
