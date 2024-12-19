# Check if List is Sorted: Determine if the list is sorted in ascending order and return a boolean.

a = [5, 1, 2, 3, 4]
b = [5, 4, 3, 2, 1]

# Here, sorted(), sort list in ascending order
print(a == sorted(a))  
print(b == sorted(b)) 

# Here, sorted(list_name, reverse = True), sort list in 
# descending order
print(a == sorted(a, reverse = True))  
print(b == sorted(b, reverse = True))