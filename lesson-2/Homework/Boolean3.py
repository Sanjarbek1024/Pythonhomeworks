# Write a program that checks if a number is positive and even.

num1 = int(input("write a number:"))

if num1 > 0 :
    print(f"{num1} is positive number")
else:
    print(f"{num1} is not positive number")

if num1 // 2 == 0 :
    print("This number is even")
else:
    print("This number is odd")