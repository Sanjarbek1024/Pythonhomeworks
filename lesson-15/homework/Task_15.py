import numpy as np

# Create a 5x5 matrix with random values
matrix_5x5 = np.random.random((5, 5))

# Find the row-wise sum
row_wise_sum = np.sum(matrix_5x5, axis=1)

# Find the column-wise sum
column_wise_sum = np.sum(matrix_5x5, axis=0)

# Print the matrix, row-wise sums, and column-wise sums
print("5x5 Matrix:")
print(matrix_5x5)

print("\nRow-wise Sums:")
print(row_wise_sum)

print("\nColumn-wise Sums:")
print(column_wise_sum)
