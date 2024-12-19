# Repeat Elements: Given a list and a number, create a new list where each element is repeated that number of times.

lst = ['super', 'great', 'hero', 'crown', 'topG', 'Peak', 'rich', 'free']
repeat = 3
 
 
# printing original list
print("The original list : " + str(lst))
 
res = []
# repeat elements repeat times

for i in lst:
    res.extend([i]*repeat)

# printing result
print("The list after adding elements : " + str(res))