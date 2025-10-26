def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
arr = [5,3,9,8,1,6,4,-10,-100]
target = 4
print(linear_search(arr, target))
# one more approach
def linear(nums, target):
    n = len(nums)
    for i in range(0, n):
        if nums[i] == target:
            return i
        return -1
nums = [10,20,25,10,10,-5,-3,-2,7]
target = 10
print(linear(nums, target))
