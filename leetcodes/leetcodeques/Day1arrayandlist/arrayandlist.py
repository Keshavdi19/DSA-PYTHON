#  Difference Between Array and List


# | Feature         | Array                                     | List                               |
# | --------------- | ----------------------------------------- | ---------------------------------- |
# | **Data Type**   | Stores **same** data type                 | Can store **different** data types |
# | **Size**        | Fixed size (defined at creation)          | Dynamic size (can grow/shrink)     |
# | **Memory**      | Stored in **contiguous** memory           | Not necessarily contiguous         |
# | **Performance** | Faster for numerical operations           | Slower in some cases               |
# | **Usage**       | Used for **performance** (numeric arrays) | Used for **flexibility**           |
# | **Example**     | `array.array('i', [1, 2, 3])`             | `[1, "hello", 3.5]`                |
# ✅ 2. Common Array Methods (Python array module)

# import array
# arr = array.array('i', [1, 2, 3, 4])
# Method	Description
# append(x)	Adds element at the end
# insert(i, x)	Inserts x at index i
# remove(x)	Removes the first occurrence of x
# pop(i)	Removes element at index i
# index(x)	Returns index of x
# reverse()	Reverses the array
# buffer_info()	Returns memory address and size
# ✅ 3. Common List Methods (Python)
# lst = [1, 2, 3, 4]
# Method	Description
# append(x)	Adds item at the end
# extend(iterable)	Adds elements from another list
# insert(i, x)	Inserts x at index i
# remove(x)	Removes first occurrence of x
# pop(i)	Removes element at index i
# sort()	Sorts the list
# reverse()	Reverses the list
# index(x)	Returns index of x
# count(x)	Counts how many times x appears
# clear()	Clears all elements
# ✅ 4. Difference Between Linear Array and Dynamic Array
# Feature	Linear Array (Static)	Dynamic Array
# Size	Fixed	Automatically resizable
# Memory	Contiguous memory block	May allocate new memory on resize
# Speed	Fast (no resizing)	Slightly slower (resizing costs time)
# Flexibility	Less flexible	Highly flexible
# Example	int arr[10]; in C	Python List, vector in C++

# 🔁 Summary
# Array: Fixed size, same data type

# List: Dynamic size, different data types

# Linear Array: Static, fixed memory

# Dynamic Array: Can grow as needed

