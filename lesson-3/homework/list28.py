# Find Minimum of Sublist: Given a list, find the minimum element of a specified sublist.

a = [[10, 13, 454, 66, 44], [10, 8, 7, 23], [3, 4, 9, 78, 54, 6]]
lis = []

# find min in list
for p in a:
	lis.append(min(p))

# Printing min
print(lis)

