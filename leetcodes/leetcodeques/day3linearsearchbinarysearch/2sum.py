def twosum(nums, target):
    n = len(nums)
    for i in range(0, n - 1):
        for j in range(0, n):
            if nums[i] + nums[j] == target:
                return [i, j]
nums = [5,9,1,2,4,1,5,6,3]
target = 11
print(twosum(nums, target))
#one more approach
def two(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        remaining  = target - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]

        hash_map[nums[i]]  = i
    return None
nums = [5,9,1,2,4,1,5,6,3] 
target = 13
print(two(nums, target))
          
