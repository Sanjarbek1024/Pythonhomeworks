import numpy as np

# Create two 3x3 matrices with random values
matrix_1 = np.random.random((3, 3))
matrix_2 = np.random.random((3, 3))

# Compute their dot product
dot_product = np.dot(matrix_1, matrix_2)

# Print the matrices and their dot product
print("Matrix 1 (3x3):")
print(matrix_1)

print("\nMatrix 2 (3x3):")
print(matrix_2)

print("\nDot Product of Matrix 1 and Matrix 2:")
print(dot_product)
