# Converting Celsius to Fahrenheit

# First finding the celsius
celsius = float(input("Enter the temperature in Celsius: "))

# Secondly, converting. C = 5/9(F-32) This is the formula of celsius in terms of fahrenheit. 
# F= 9C/5 + 32

fahrenheit = (celsius * 9 / 5) + 32

# Finally result

print(f"This is the Fahrenheit temperature: {fahrenheit}")

