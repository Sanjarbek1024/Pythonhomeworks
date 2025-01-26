# Given equation:
# 10L1 - 2L2 + 3L3 = 12
# -2L1 + 8L2 - L3 = -5
# 3L1 - L2 + 6L3 = 15

import numpy as np

# We need to define the coefficients and constants of the system of equations
coefficients = np.array([[10, -2, 3],
                         [-2, 8, -1],
                         [3, -1, 6]])

constants = np.array([12, -5, 15])

# To solve the system of equations, we need to use the function np.linalg.solve()
solution = np.linalg.solve(coefficients, constants)

# Print the solution
print("The solution is:", solution)