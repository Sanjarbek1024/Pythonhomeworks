# First Element: Access the first element of a list, considering what to return if the list is empty.

list = [1, 3, 4, 6, 4, 7, 8, 9]

first = list[0]

if first:
    print(f"{first} is the first element in the list")
else:
    print("There is not element in the list")