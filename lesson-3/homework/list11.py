# Remove Duplicates: Given a list, create a new list that contains only unique elements from the original list.

lists = ['apple', 'cheese', 'cheap', 'ice', 'pink', 'ice', 'apple', 'cherry', 'cheap', 'apple']

b = list(set(lists))
print(b)    # ['apple', 'pink', 'ice', 'cheese', 'cheap', 'cherry']