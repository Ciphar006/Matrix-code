import numpy as np

def rank(matrix):
  """Returns the rank of a matrix."""
  determinant = np.linalg.det(matrix)
  if determinant != 0:
    return matrix.shape[0]
  else:
    minors = [np.linalg.det(matrix_minor) for matrix_minor in matrix.minors()]
    return max(minors, default=0)

matrix = np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9]])
rank_of_matrix = rank(matrix)
print(rank_of_matrix)