# fibonacci
# 0 1 1 2 3 5 8 13 21 34

class Slotiin:
    def func(self, num):
        if num == 0 or num == 1:
            return num
        return self.func(num - 1) + self.func(num - 2)

    def fib(self, n: int) -> int:
        answer = self.func(n)
        return answer

s = Slotiin()
print(s.fib(6))   # Output: 8
# one more way to solve this problem
def func(num):
    if num == 0 or num == 1:
        return num
    return func(num - 1) + func(num - 2)

def fib(n):
    return func(n)

print(fib(6))   # Output: 8
# one more way to solve this problem
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(6))
