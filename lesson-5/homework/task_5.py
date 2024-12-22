# Define a function is_prime(n) which returns True if the given n(n > 0) is prime number, otherwise returns False.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a positive integer: "))
if is_prime(n):
    print(f"{n} is a prime number")