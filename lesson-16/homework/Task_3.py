# The system of equations is given:
#     4x + 5and +6with = 7
#     3x - and + with = 4
#     2x + and - 2with = 5


import numpy as np

# We need to define the coefficients and constants of the system of equations
coefficients = np.array([[4, 5, 6], 
                         [3, -1, 1], 
                         [2, 1, -2]])
constants = np.array([7, 4, 5])

# To solve the system of equations, we need to use the function np.linalg.solve()
solution = np.linalg.solve(coefficients, constants)

# Print the solution
print("The solution is:", solution)