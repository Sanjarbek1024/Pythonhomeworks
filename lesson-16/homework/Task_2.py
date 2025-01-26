import numpy as np

# Custom function to calculate the power
@np.vectorize
def calculate_power(base, power):
    """Calculates the power of a number. As well it is a vectorized function."""
    return base ** power

# Arrays of numbers and powers
numbers = np.array([2, 3, 4, 5])
powers = np.array([1, 2, 3, 4])

# Apply the function to the arrays
results = calculate_power(numbers, powers)

# Print the results
print("Base numbers:", numbers)
print("Powers:", powers)
print("Results:", results)
