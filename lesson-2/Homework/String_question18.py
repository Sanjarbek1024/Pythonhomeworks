# Write a program that checks if a string starts with one word and ends with another.
# Example:

# Input: "Python is fun!"
# Starts with: "Python"
# Ends with: "fun!"

matn = str(input("enter something: "))

words = matn.split()
word1 = words[0]
word2 = words[-1]

if word1 == word2:
   print("First and last words are the same")
else: 
   print("The first and last words are different")