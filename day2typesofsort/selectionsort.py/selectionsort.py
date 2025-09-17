def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):       # har position ke liye
        min_index = i          # assume karo current element hi minimum hai
        for j in range(i+1, n):  
            if arr[j] < arr[min_index]:   # agar chhota element milta hai
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # swap
    return arr


# User input
user_input = input("Array ke elements space se alag karke likho: ")
arr = list(map(int, user_input.split()))

print("Original Array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted Array (Selection Sort):", sorted_arr)
