import numpy as np

# Create a 5x5 random matrix
random_matrix = np.random.random((5, 5))

# Normalize the matrix
# Formula: normalized_value = (value - min) / (max - min)
normalized_matrix = (random_matrix - random_matrix.min()) / (random_matrix.max() - random_matrix.min())

# Print the original and normalized matrix
print("Original 5x5 Random Matrix:")
print(random_matrix)

print("\nNormalized 5x5 Matrix:")
print(normalized_matrix)
