def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1
print(partition([3,6,8,10,1,2,1], 0, 6))  # Example usage
def quicksort(nums, low, high):
    if low < high:
        pi = partition(nums, low, high)
        quicksort(nums, low, pi - 1)
        quicksort(nums, pi + 1, high)
    return nums
print(quicksort([3,6,8,10,1,2,1], 0, 6))  # Example usage

