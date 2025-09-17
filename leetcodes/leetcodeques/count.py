n = 5438
num  = n
count = 0
while num > 0:
    count += 1
    num = num // 10
print("The number of digits in", n, "is", count)
# one more way to solve this problem
from math import *
def count_digits(num):
    return int(log10(num)) + 1
print("The number of digits in", n, "is", count_digits(n))