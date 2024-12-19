# Check Palindrome: Given a list, check if the list is a palindrome (reads the same forwards and backwards).

s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

c = s[::-1]
g = d[::-1]
print(s == c)
print(g == d)