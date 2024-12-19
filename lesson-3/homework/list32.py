# Merge and Sort: Given two lists, create a new sorted list that merges both lists.

a = [2, 4, 6, 7, 9, 34, 6]
b = [1, 2, 5, 4, 3, 7, 9, 6]

combined = a + b
a.extend(b)


print(a)
print(combined)

a.sort()
print(a)





