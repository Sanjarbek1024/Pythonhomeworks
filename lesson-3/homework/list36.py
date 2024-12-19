# Sum of Positive Numbers: Given a list of numbers, calculate the sum of all positive numbers.

numbers = [6, 9, -7, 3, 4, -5, 2, -1, 6, -34, 9, 7, -6, 4, 2]

positive = []

for x in numbers:
    if x > 0:
        positive.append(x)

print(sum(positive))