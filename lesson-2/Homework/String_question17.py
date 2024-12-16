# Ask the user for a string and replace all the vowels with a symbol (e.g., *).

matn = str(input(" Enter a string: "))

vowels = "aeiouAEIOU"

string = "".join('*' if char in vowels else char for char in matn)

print("String after replacing vowels:", string)