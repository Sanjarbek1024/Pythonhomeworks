#Ask the user for a sentence and create an acronym from the first letters of each word.
#Example:

#Input: "World Health Organization"
#Output: "WHO"

sentence = input("Enter a string: ")
words = sentence.split()

acronim = "".join(word[0].upper() for word in words)
print(f"The acronim of the string is that: {acronim}")
