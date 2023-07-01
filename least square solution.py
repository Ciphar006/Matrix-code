import numpy as np

def least_squares(x_i, b_i):
  """Returns the least squares solution for the closest line to the points."""
  b = np.mean(b_i)
  θ = 0
  RSS = 0
  for i in range(len(x_i)):
    b_predicted = b + θ * x_i[i]
    RSS += (b_predicted - b_i[i])**2
  partial_b = 2 * (b - b_i)
  partial_θ = 2 * (b_predicted - b_i) * x_i[i]
  equations = [partial_b, partial_θ]
  solutions = np.linalg.solve(equations, [1, 1])
  b = solutions[0]
  θ = solutions[1]
  return (b, θ)

x_i = [1, -1, 3]
b_i = [6, 3, 15]
least_squares_solution = least_squares(x_i, b_i)
print(least_squares_solution)