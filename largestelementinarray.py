nums = [44, 55, 66, 77, 88, 99]
largest = nums[0]
n = len(nums)
for i in range(1, n):
    largest = max(largest, nums[i])
print("The largest element in the array is:", largest)
# one more method
print(max(nums))
