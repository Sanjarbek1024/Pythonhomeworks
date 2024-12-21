# 6. Prime Numbers Task: Write a Python program that prints all prime numbers between 1 and 100.

# A prime number is a number greater than 1 that is not divisible by any number other than 1 and itself. Use nested loops to check divisibility.

prime_numbers = []
for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        prime_numbers.append(num)

print(prime_numbers)

# output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]