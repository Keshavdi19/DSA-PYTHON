def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge_array(left_half, right_half)
def merge_array(left, right):
    if not left:
        return right
    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge_array(left[1:], right)
    else:
        return [right[0]] + merge_array(left, right[1:])
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))