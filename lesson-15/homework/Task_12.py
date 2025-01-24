import numpy as np

# Create matrix A (3x4) and matrix B (4x3)
matrix_A = np.random.random((3, 4))
matrix_B = np.random.random((4, 3))

# Compute the matrix product A . B
matrix_product = np.dot(matrix_A, matrix_B)

# Print matrix A, matrix B, and their product
print("Matrix A (3x4):")
print(matrix_A)

print("\nMatrix B (4x3):")
print(matrix_B)

print("\nMatrix Product A . B (3x3):")
print(matrix_product)
