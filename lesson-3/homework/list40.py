# Get Unique Elements in Order: Given a list, create a new list that contains unique elements while maintaining the original order.

original = [1, 7, 8, 4, 7, 2, 5, 2, 3, 4, 4, 5]
unique = []
seen = set()  

for element in original:
    if element not in seen:
        unique.append(element)
        seen.add(element)

print(unique)