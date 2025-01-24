import numpy as np

# Create a 5x3 matrix and a 3x2 matrix
matrix_5x3 = np.random.random((5, 3))
matrix_3x2 = np.random.random((3, 2))

# Perform the matrix multiplication
result_matrix = np.dot(matrix_5x3, matrix_3x2)

# Print the matrices and the result
print("5x3 Matrix:")
print(matrix_5x3)

print("\n3x2 Matrix:")
print(matrix_3x2)

print("\nResult of Matrix Multiplication (5x2):")
print(result_matrix)
