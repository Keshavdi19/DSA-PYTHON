n = 5438
num  = n
count = 0
while num > 0:
    count += 1
    num = num // 10
print("The number of digits in", n, "is", count)
