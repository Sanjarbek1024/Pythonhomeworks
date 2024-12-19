# Sum of Negative Numbers: Given a list of numbers, calculate the sum of all negative numbers.


numbers = [6, 9, -6, 3, 4, -5, 2, -1, 6, -34, 9, 7, -6, 4, 2]

negative = []
for x in numbers:
    if x < 0:
        negative.append(x)

print(sum(negative))