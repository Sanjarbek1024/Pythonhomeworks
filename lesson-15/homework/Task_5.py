import numpy as np

# Create a 10x10 array with random values
random_array_10x10 = np.random.random((10, 10))

# Find the minimum and maximum values
min_value = random_array_10x10.min()
max_value = random_array_10x10.max()

# Print the array, minimum and maximum values
print("10x10 Array with Random Values:")
print(random_array_10x10)
print("\nMinimum Value:", min_value)
print("Maximum Value:", max_value)
