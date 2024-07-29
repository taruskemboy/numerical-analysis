import numpy as np

def lagrange_interpolation(x, data):
  """Computes the coefficients of the Lagrange polynomial that interpolates the given data points.

  Args:
    x: The x-values of the data points.
    data: The y-values of the data points.

  Returns:
    The coefficients of the Lagrange polynomial.
  """

  n = len(x)
  L = np.zeros((n, n))

  for i in range(n):
    for j in range(n):
      if i != j:
        L[i, j] = 1 / (x[i] - x[j])

  for i in range(n):
    for j in range(n):
      if i != j:
        L[i, i] *= np.prod([x[i] - x[k] for k in range(n) if k != i and k != j])

  coeffs = np.dot(L, data)
  return coeffs

# Example usage:
x_data = np.array([1, 2, 3, 4])
y_data = np.array([1, 4, 9, 16])

lagrange_coeffs = lagrange_interpolation(x_data, y_data)
print(lagrange_coeffs)
