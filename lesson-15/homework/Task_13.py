import numpy as np

# Create a 3x3 random matrix and a 3-element column vector
matrix_3x3 = np.random.random((3, 3))
column_vector = np.random.random((3, 1))

# Compute the matrix-vector product
result = np.dot(matrix_3x3, column_vector)

# Print the matrix, column vector, and the result of the matrix-vector product
print("3x3 Matrix:")
print(matrix_3x3)

print("\n3-element Column Vector:")
print(column_vector)

print("\nMatrix-Vector Product:")
print(result)
