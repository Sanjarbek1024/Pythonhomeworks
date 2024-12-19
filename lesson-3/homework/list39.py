# Create Nested List: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.

original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sublist = 3

nested = []

# Ro'yxatni bo'laklarga bo'lamiz
for i in range(0, len(original), sublist):
    nested.append(original[i:i + sublist])

print(nested)