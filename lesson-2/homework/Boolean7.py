# Write a program that checks if the sum of two numbers is greater than 50.8. Create a program that checks if a given number is between 10 and 20 (inclusive)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 + num2 > 50.8:
    print("The sum of the given numbers are greater than 50.8")
else:
    print("The sum of these numbers are less than 50.8")



    # SECOND

    number = float(input("Enter a number: "))

    if number >= 10 and number <= 20 :
     print(f"{number} is between 10 and 20.")
    else:
      print(f"{number} is NOT between 10 and 20.")