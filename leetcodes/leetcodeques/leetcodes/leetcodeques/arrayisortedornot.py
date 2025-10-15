def checking(nums):
    n = len(nums)
    for i in range(0, n-1):
        if nums[i] > nums[i+1]:
            return False
    return True
print(checking([1,4,6,7]))

