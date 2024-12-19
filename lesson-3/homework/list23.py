# Filter Odd Numbers: Given a list of integers, create a new list that contains only the odd numbers.

test = [5, 6, 1, 8, 2, 1, 9, 10, 7, 1]

new_list = []

for num in test:
    if num % 2 == 1:
        new_list.extend([num])

print("the even numbers:", new_list)