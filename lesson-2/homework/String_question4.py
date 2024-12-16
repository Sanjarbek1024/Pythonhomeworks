# Write a Python program to check if a given string is palindrome or not.

word = input("Enter a string to check if it is a palindrome: ")

# Now we convert all digits into lowercases and remove

word1 = word.replace(" ", "").lower()

if word1 == word1[::-1]:
       print(f"{word} is a palindrome")
else:
         print(f"{word} is not a palindrome")