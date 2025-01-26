import numpy as np

# Defining the function
@np.vectorize
def convert(fahrenheit):
    """Converts a temperature in Fahrenheit to Celsius. Also it is a vectorized function."""
    return (fahrenheit - 32) * 5 / 9

# Array of temperatures in Fahrenheit
fahrenheit_array = np.array([32, 68, 100, 212, 77])

# Apply the function to the array
celsius_arrey = convert(fahrenheit_array)

# The results
print("Temperatures in Fahrenheit:", fahrenheit_array)
print("Temperatures in Celsius:", celsius_arrey)
