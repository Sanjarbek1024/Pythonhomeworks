# Create a program that accepts a number and returns the last digit of that number.

# first step
number = int(input("Enter a number: "))

# Second step is the most important part. For finding the last digit, we should devide the number to 10, and remainder is last digit. For negative numbers we take the absolute value of the number.

last_digit = abs(number) % 10

# Result
print(f"The last digit of the number is that: {last_digit}")

#that's it