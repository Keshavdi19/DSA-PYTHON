def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):       # har position ke liye
        min_index = i          # assume karo current element hi minimum hai
        for j in range(i+1, n):  
            if arr[j] < arr[min_index]:   # agar chhota element milta hai
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # swap
    return arr
print(selection_sort([2,1,3,4,5,6]))

