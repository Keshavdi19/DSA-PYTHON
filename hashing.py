n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 0]
m = [10, 11, 1, 9, 5, 67, 2]
for num in m:
    count = 0
    for i in n:
        if i == num:
            count += 1 
    print(count)
