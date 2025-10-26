def func(i, n):
    if i  > n:
        return
    func(i + 1, n)
    print(i)
func(1, 4)
# one more way opposite to it
def func2(i, N):
    if i  > N:
        return
    print(i)
    func2(i + 1, N)
    
func2(1, 4)
# one more way
def func1(i, z):
    if i  <  1:

        return
    print(i)
    func1(i - 1, z)
    
func1(4, 4)