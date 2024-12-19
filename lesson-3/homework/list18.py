# Find Sublist: Given a list and a sublist, check if the sublist exists within the list.

test_test = [5, 6, 3, 8, 2, 1, 7, 1]

print("The original list : " + str(test_list))

sublist = [8, 2, 7]

if set(sublist).intersection(set(test_list)) == set(sublist):
    res = True
else:
    res = False

# printing result
print("Is sublist present in list ? : " + str(res))