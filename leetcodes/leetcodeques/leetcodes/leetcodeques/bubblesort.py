def bubble(nums):
    n = len(nums)
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# Example
print(bubble([5, 3, 8, 1, 2]))
#average case