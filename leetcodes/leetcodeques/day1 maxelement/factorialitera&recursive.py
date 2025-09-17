def fact_iter(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
print(fact_iter(5))
def fact_rec(n):
    if n==0 or n==1:
        return 1
    return n * fact_rec(n-1)
print(fact_rec(6))
