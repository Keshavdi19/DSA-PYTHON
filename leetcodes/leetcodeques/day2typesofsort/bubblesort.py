def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):           # Outer loop (passes)
        for j in range(n-i-1):     # Inner loop (comparisons)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# Example: 5 3 8 4 2
user_input = input("write the array separate without comma: ")

arr = list(map(int, user_input.split()))


sorted_arr = bubble_sort(arr)

print("Sorted Array:", sorted_arr)
