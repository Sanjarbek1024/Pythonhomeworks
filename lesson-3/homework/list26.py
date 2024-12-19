# Get Middle Element: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.

lst = ['super', 'great', 'hero', 'crown', 'topG', 'Peak', 'rich', 'free']

# first find the numbers of elements
a = len(lst)
b = a // 2

if a % 2 == 0:
    print(lst[b - 1:b + 1])
else:
    print(lst[b])