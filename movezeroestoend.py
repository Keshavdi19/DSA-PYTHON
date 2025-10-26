def Move_Zeroes(nums):
    n = len(nums)
    temp = []
    for i in range(0, n):
        if nums[i]  != 0:
            temp.append(nums[i])
    nz = len(temp)
    for i in range(0, nz):
        nums[i] = temp[i]
    for i in range(nz, n):
        nums[i] = 0
    return nums
print(Move_Zeroes([1,0,3,2,0,2,0]))
# one more optimized approach
def Move_Zeroes_Optimized(nums):
    if len(nums) == 1:
        return nums
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            break
        i += 1
    if i == len(nums):
        return nums
    j = i + 1
    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    return nums
print(Move_Zeroes_Optimized([1,0,3,2,0,2,0]))
    
