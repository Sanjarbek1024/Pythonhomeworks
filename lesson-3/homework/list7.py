# Last Element: Access the last element of a list, considering what to return if the list is empty.

list = [1, 3, 4, 6, 4, 7, 8, 9, 7]

last = list[-1]

if last:
    print(f"{last} is the last element in the list")
else:
    print("There is not element in the list")