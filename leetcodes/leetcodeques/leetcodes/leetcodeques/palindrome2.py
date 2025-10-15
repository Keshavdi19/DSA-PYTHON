# check if a string is palindrome or not
def is_palindrome(s):
    n = len(s)
    left = 0
    right = n - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
print(is_palindrome("ABA"))

  






 





                         

