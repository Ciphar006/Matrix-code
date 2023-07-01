import numpy as np

def projection(vector1, vector2):
  """Returns the projection of vector1 along vector2."""
  dot_product = np.dot(vector1, vector2)
  magnitude_of_vector2 = np.linalg.norm(vector2)
  projection = dot_product / magnitude_of_vector2**2 * vector2
  return projection

vector1 = np.array([5, -4, 1])
vector2 = np.array([3, -2, 4])
projection = projection(vector1, vector2)
print(projection)