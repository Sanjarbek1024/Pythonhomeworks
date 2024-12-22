# Write a script called temperature.py that defines two functions:

# convert_cel_to_far() which takes one float parameter representing degrees Celsius and returns a float representing the same temperature in degrees Fahrenheit using the following formula: F = C * 9/5 + 32
# convert_far_to_cel() which take one float parameter representing degrees Fahrenheit and returns a float representing the same temperature in degrees Celsius using the following formula: C = (F - 32) * 5/9

# The script should first prompt the user to enter a temperature in degrees Fahrenheit and then display the temperature converted to Celsius. Then prompt the user to enter a temperature in degrees Celsius and display the temperature converted to Fahrenheit. All converted temperatures should be rounded to 2 decimal places.

# Here’s a sample run of the program:



def convert_cel_to_far(cel):
    return cel * 9/5 + 32



def convert_far_to_cel(far):
    return (far - 32) * 5/9


cel = float(input("Enter a temperature in degrees Celsius: "))
far = convert_cel_to_far(cel)

print(f"{cel}°C is equal to {far:.2f}°F")

far = float(input("Enter a temperature in degrees Fahrenheit: "))
cel = convert_far_to_cel(far)

print(f"{far}°F is equal to {cel:.2f}°C")


# output
# Enter a temperature in degrees Celsius: 37
# 37.0°C is equal to 98.60°F
# Enter a temperature in degrees Fahrenheit: 72
# 72.0°F is equal to 22.22°C