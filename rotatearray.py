def rotate(nums, k):
    n = len(nums)
    rotations = k % n
    for i in range(0, rotations):
        p = nums.pop()
        nums.insert(0, p)
    return nums
print(rotate([2,4,5,6,1],3))
# one more way 
def Rotate(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[n-k:] + nums[:n-k]
    return nums
print(Rotate([1,2,3,4,5],2))
# another approach
def rotateArray(nums, k):
    n = len(nums)
    k = k % n
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums
print(rotateArray([1,2,3,4,5],2))
# another approach
# reverse function
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
def rotateArr(nums, k):
    n = len(nums)
    k = k % n
    reverse(nums, 0, n-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)
    return nums
print(rotateArr([1,2,3,4,5],2))