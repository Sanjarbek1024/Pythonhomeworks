# Find Maximum of Sublist: Given a list, find the maximum element of a specified sublist.

a = [[10, 13, 454, 66, 44], [10, 8, 7, 23], [3, 4, 9, 78, 54, 6]]
lis = []

# find max in list
for p in a:
	lis.append(max(p))

# Printing max
print(lis)
