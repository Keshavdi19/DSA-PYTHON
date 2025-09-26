# print x n times is the question
def func(x, n):
    if n == 0:
       return 
    print(x)
    func(x, n-1)
func(15, 4)
# print 1 to n using recursion
def func1(i, N):
    if i > N:
        return
    print(i)
    func1(i+1, N)
func1(1, 4)
    
    





    