import numpy as np

def is_in_null_space(matrix, vector):
  """Returns True if vector is in the null space of matrix."""
  product = np.dot(matrix, vector)
  if product == np.zeros(product.shape):
    return True
  else:
    return False

matrix = np.array([[2, 1, 1, 0], [4, 3, 1, 0], [6, 0, 6, 0], [8, 5, 3, 0]])
vector1 = np.array([1, 3, 1, 0])
vector2 = np.array([0, -1, 0, 1])

if is_in_null_space(matrix, vector1) and is_in_null_space(matrix, vector2):
  print("The vectors are in the null space.")
else:
  print("The vectors are not in the null space.")