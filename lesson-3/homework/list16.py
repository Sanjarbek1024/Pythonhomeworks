# Count Odd Numbers: Given a list of integers, count how many of them are odd.

a = [5, 6, 8, 7, 7, 9, 23, 65, 77, 80, 40]

Odd = 0
Even = 0

for num in a:

    if num % 2 == 1:
        Odd += 1
    else:
        Even += 1

# Natija
print("The number of odd numbers :", Odd)