def missing(nums):
    n = len(nums)
    for i in range(0, n+1):
        if i not in nums:
            return i
print(missing([9,6,4,2,3,5,7,0,1]))
# one more approach
def missed(nums):
    n = len(nums)
    freq = {}
    for i in range(0, n+1):
        freq[i] = 0
    for num in nums:
        freq[num] = 1
    for k,v in freq.items():
        if v == 0:
            return k
print(missed([9,6,4,2,3,5,7,0,1]))
# optimal solution using sum formula
def miss(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    sum_of_nums = sum(nums)
    return total - sum_of_nums
print(miss([9,6,4,2,3,5,7,0,1]))



    