# Find Second Largest: From a given list, find the second largest element.

test = [5, 6, 1, 8, 2, 1, 7, 1]


a = list(set(test))

print("The sorted version of the list:", a)
# The sorted version of the list: [8, 7, 6, 5, 2, 1, 1, 1]


print(a[-1])