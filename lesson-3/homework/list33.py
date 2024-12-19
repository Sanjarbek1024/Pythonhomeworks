# Find All Indices: Given a list and an element, find all the indices of that element in the list.

lists = [2, 4, 6, 7, 9, 34, 6, 1, 2, 5, 4, 3, 7, 9, 6]
element = 6

indices = []
for i in range(len(lists)):
    if lists[i] == element:
        indices.append(i)

print(indices)