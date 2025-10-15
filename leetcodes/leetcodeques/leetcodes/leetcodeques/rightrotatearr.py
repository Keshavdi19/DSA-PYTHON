def right_rotate(nums):
    n = len(nums)
    nums = nums[-1:] + nums[0:n-1]
    return nums
print(right_rotate([1,2,3,4,5]))  # Output: [5,1,2,3,4]
# one more approach
def Right(num):
    n = len(num)
    temp = num[n-1]
    for i in range(n-2, -1, -1):
        num[i+1] = num[i]
    num[0] = temp
    return num
print(Right([1,2,3,4,5]))







