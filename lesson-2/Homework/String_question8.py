# Write a program that asks the user for a string and prints the first and last characters of the string.

word = str(input(" Enter a string to know first and last characters of the string: "))

first = word[:1]
last = word[-1:]

print(f"First character of the string is: {first}")
print(f"The last character of the string is: {last}")