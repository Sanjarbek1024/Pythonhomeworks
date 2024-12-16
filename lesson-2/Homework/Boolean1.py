# Write a program that accepts a username and password and checks if both are not empty

username = input("Enter your username: ")

# Ask the user for a password
password = input("Enter your password: ")

# Check if both username and password are not empty
if username.strip() and password.strip():            # i've used chatgpt to know this 
    print("Login successful!")
else:
    print("Error: Username and password cannot be empty.")