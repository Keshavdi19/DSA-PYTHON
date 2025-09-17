import math

def get_factors(num):
  """
  This function finds all the factors of a given number.

  Args:
    num: An integer for which to find the factors.

  Returns:
    A sorted list of all factors of the number.
  """
  result = []
  # Iterate from 1 up to the square root of the number
  for i in range(1, int(math.sqrt(num)) + 1):
    # If i is a divisor of num, then it's a factor
    if num % i == 0:
      result.append(i)
      # Add the corresponding factor (num/i)
      # This check prevents adding the square root twice for perfect squares
      if num // i != i:
        result.append(num // i)
  
  result.sort()
  return result

# --- Example Usage ---
number_to_factor = 100
factors = get_factors(number_to_factor)
print(f"The factors of {number_to_factor} are: {factors}")
# Expected Output: The factors of 100 are: [1, 2, 4, 5, 10, 20, 25, 50, 100]

number_to_factor = 36
factors = get_factors(number_to_factor)
print(f"The factors of {number_to_factor} are: {factors}")
# Expected Output: The factors of 36 are: [1, 2, 3, 4, 6, 9, 12, 18, 36]