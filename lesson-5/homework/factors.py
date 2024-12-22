# Enter a positive integer: 12
# 1 is a factor of 12
# 2 is a factor of 12
# 3 is a factor of 12
# 4 is a factor of 12
# 6 is a factor of 12
# 12 is a factor of 12

def factors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(f"{i} is a factor of {num}")

print(factors(12))

# output
# Enter a positive integer: 12
# 1 is a factor of 12
# 2 is a factor of 12
# 3 is a factor of 12
# 4 is a factor of 12
# 6 is a factor of 12
# 12 is a factor of 12
# None