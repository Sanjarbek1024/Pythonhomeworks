# Write a program that takes a list of words and joins them into a single string, separated by a character

lists = "Apple banana orange potato cherry pink"
print(lists.replace(" ", "-"))

print(lists.replace(" ", ","))

# Agar boshida " " bolsa , buni qollaniladi

list2 = "  Apple banana orange potato cherry pink  "
matn = list2.strip()
print(matn.replace(" ", ","))
print(matn.replace(" ", "-"))