import numpy as np

# Create a 3x3 matrix with random values
matrix_3x3 = np.random.random((3, 3))

# Calculate the determinant of the matrix
determinant = np.linalg.det(matrix_3x3)

# Print the matrix and its determinant
print("3x3 Matrix:")
print(matrix_3x3)

print("\nDeterminant of the Matrix:", determinant)
