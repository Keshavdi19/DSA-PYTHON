def func1(i, n):
    if i > n:
        return
    func1(i+1, n)
    print(i)
func1(1, 4)

