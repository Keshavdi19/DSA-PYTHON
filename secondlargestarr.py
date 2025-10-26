nums = [55, 32, 97, 11, 10]
nums.sort()
n = len(nums)
print(nums[n-2])
# one more way
num = [55, 32, 97, -55, 45, 31, 21]
largest = float("-inf")
se_largest = float("-inf")
n = len(nums)
for i in range(0, n):
    largest = max(largest, nums[i])
for i in range(0, n):
    if nums[i] > se_largest and nums[i] != largest:
        se_largest = nums[i]
print(se_largest)
# one more way
numb = [55, 32, 97, -55, 45, 31, 88, 21]
largest = float("-inf")
s_largest = float("-inf")
n = len(numb)
for i in range(0, n):
    if numb[i] > largest:
        s_largest = largest
        largest = numb[i]
    elif numb[i] > s_largest and numb[i] != largest:
        s_largest = numb[i]
print(s_largest)



