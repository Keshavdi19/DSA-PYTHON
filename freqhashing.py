nums = [5,1,2,3,5,6,7,111,3,4,7,8,9]
freq_map = {}
for i in range(0, len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1
print(freq_map)
# one more way to solve thia problem
numbers = [5,1,2,3,5,6,7,111,3,4,7,8,9]
hash_map = {}
n = len(numbers)
for i in range(0, n):
    hash_map[numbers[i]] = hash_map.get(numbers[i], 0) + 1
print(hash_map)


