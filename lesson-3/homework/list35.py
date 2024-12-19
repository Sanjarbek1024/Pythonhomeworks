# Create Range List: Create a list of numbers in a specified range (e.g., from 1 to 10).

my_list = []

start, end = 1, 10

if start < end:
    my_list.extend(range(1, 11))

print(my_list)