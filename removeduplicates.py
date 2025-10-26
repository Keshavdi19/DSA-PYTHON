def remove(nums):
    n = len(nums)
    freq_map = {}
    for i in range(0, n):
        num = nums[i]
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    index = 0
    for key in freq_map:
        nums[index] = key
        index += 1
    return index
print(remove([1,1,2]))  # Output: 2
# one more approach
def remove_duplicates(nums):
    n = len(nums)
    freq_map = {}
    for i in range(0, n):
        freq_map[nums[i]] = 0
    index = 0
    for key in freq_map:
        nums[index] = key
        index += 1
    return index
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4,5])) 
# one more approach two pointer approach
def remove_duplicates_in_place(nums):
    n = len(nums)
    if n == 1:
        return 1
    i = 0
    j = i + 1
    while j < n:
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
        j += 1
    return i + 1
print(remove_duplicates_in_place([0,0,1,1,1,2,2,3,3,4]))  
   