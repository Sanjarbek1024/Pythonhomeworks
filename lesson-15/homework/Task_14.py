import numpy as np

# Create a 3x3 matrix A and a 3x1 column vector b
A = np.random.random((3, 3))
b = np.random.random((3, 1))

# Solve the linear system Ax = b
x = np.linalg.solve(A, b)

# Print the matrix A, vector b, and the solution vector x
print("Matrix A (3x3):")
print(A)

print("\nColumn Vector b (3x1):")
print(b)

print("\nSolution Vector x (3x1):")
print(x)
