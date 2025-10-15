def insertion(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j>=0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums
print(insertion([5, 3, 8, 1, 2]))
# other
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