def subarraysum(nums):
    n = len(nums)
    maxi = float("-inf")
    for i in range(0, n):
        total = 0
        for j in range(i, n):
            total = total + nums[j]
            maxi = max(maxi, total)
    return maxi
print(subarraysum([-2,1,-3,4,-1,2,1,-5,4]))
# one more approach'
def sub(nums):
    nz = len(nums)
    maxim = float("-inf")
    total = 0
    for i in range(0, nz):
        total = total + nums[i]
        maxim = max(maxim, total)
        if total < 0:
            total = 0
    return maxim
print(sub([-2,1,-3,4,-1,2,1,-5,4]))


