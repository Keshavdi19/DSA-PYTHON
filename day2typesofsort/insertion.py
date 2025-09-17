def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):       # 1st element ko sorted maan kar chalte hain
        key = arr[i]            # current element
        j = i - 1
        while j >= 0 and arr[j] > key:   # peeche ke elements ko shift karo
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key        # key ko sahi jagah insert karo
    return arr   
# User input
user_input = input("Array ke elements space se alag karke likho: ")
arr = list(map(int, user_input.split()))

print("Original Array:", arr)
sorted_arr = insertion_sort(arr)
print("Sorted Array (Insertion Sort):", sorted_arr)
