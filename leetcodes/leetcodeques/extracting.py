def extract_digits(num):
    while num > 0:
        last_digit = num % 10
        print(last_digit)
        num = num // 10  # Extracting digits of a number
        

extract_digits(5873)
