def linear_search(arr, target):
    for i in (len(arr)):
        if arr[i] == target:
            return i
    return -i
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search([10, 20, 30, 40], 30))  # Output: 2


