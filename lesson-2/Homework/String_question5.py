# Write a program that counts the number of vowels and consonants in a given string.

text = str(input("Enter a word to know the numbers of vowels and consonants:"))

a = text.count("a")
A = text.count("A")
e = text.count("e")
E = text.count("E")
i = text.count("i")
I = text.count("I")
o = text.count("o")
O = text.count("O")
u = text.count("u")
U = text.count("U") 

vowels = a + A + e + E + i + I + o + O + u + U

print(f"The given string is that: {text}")
print(f"The numbers of vowels in given string: {vowels}")

# The numbers of consonants

spaceles = text.replace(" ","")
spaceless = len(spaceles)
consonants = spaceless - vowels

# Final result
print(f"The number of consonants in the given string: {consonants}")

# Birinchi unlilarning sonini topib oldim, va uni print qildim. Keyin Hamma bo'sh joylarni chiqarib tashladim, va umumiy harflarning sonini topdim. Keyin Umumiydan unlilarni ayirdim.
# Faqat bitta narsani qila olmadim, tinish belgilarini chiqara olmadim.
