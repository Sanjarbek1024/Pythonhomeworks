# Count Even Numbers: Given a list of integers, count how many of them are even.

a = [5, 6, 8, 7, 7, 9, 23, 65, 77, 80, 40]

even = 0
odd = 0

for num in a:    
  
    # Checking if the number is even
    if num % 2 == 0:  
        even += 1
    else:  
        odd += 1

# Results
print("Even numbers:", even)
print("Odd numbers:", odd)

