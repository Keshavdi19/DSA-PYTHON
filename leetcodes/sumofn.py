# recursive way
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n-1)
print(sum_n(4))
# formula
def sum(n):
    return n*(n+1)//2
print(sum(4))
# loop
# Sum of first n numbers using loop

# Step 1: input lo
n = int(input("Enter a number: "))

# Step 2: total variable banao
total = 0

# Step 3: loop chalao 1 se n tak
for i in range(1, n+1):
    total = total + i   # har step pe add karo

# Step 4: result print karo
print("Sum of first", n, "numbers is:", total)
