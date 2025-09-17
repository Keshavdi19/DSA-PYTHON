arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
n = len(arr)

# Right Rotate
right_rotated = arr[-k:] + arr[:-k]
print("Right Rotate:", right_rotated)

# Left Rotate
left_rotated = arr[k:] + arr[:k]
print("Left Rotate:", left_rotated)

