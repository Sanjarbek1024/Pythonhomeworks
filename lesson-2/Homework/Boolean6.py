# Create a program that accepts a number and checks if it’s divisible by both 3 and 5.

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
        print(True)
else:
        print(False)