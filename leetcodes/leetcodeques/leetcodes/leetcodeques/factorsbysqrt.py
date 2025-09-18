from math import sqrt
result = []
for i in range(1, int(sqrt(36)) + 1):
    if 36 % i == 0:
        result.append(i)
        if 36 // i != i:
            result.append(36 // i)
result.sort()
print(result)  # Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]