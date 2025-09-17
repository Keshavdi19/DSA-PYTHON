# Step 1: empty stack banao
stack = []

# Step 2: user input lo (space se alag values)
user_input = input("Enter numbers separated by space: ")

# Step 3: convert input string into list of integers
numbers = list(map(int, user_input.split()))

# Step 4: har number ko stack me push karo
for num in numbers:
    stack.append(num)

# Step 5: stack print karo
print("Stack after pushing:", stack)

# Step 6: ek element pop karo (agar stack khaali nahi hai)
if len(stack) > 0:
    removed = stack.pop()
    print("Popped element:", removed)

# Step 7: final stack print karo
print("Stack after popping:", stack)


