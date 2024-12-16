# Create a program to ask name and year of birth from user and tell them their age.

# Questions

name = str(input("What is your name: "))
birthdate = int(input("What is the year of your birth: "))

# Second step is calculating the age
age = 2024 - birthdate

# final step.
print(f"{name} is {age} years old")