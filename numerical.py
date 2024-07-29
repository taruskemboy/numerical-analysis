# Step 1: Install scipy
pip nstall scipy

# Step 2: Import the necessary modules
import numpy as np
from scipy.integrate import quad

# Step 3: Define the function
def integrand(x):
    return np.exp(-x**2)

# Step 4: Define the limits of integration
a = 0
b = 1

# Step 5: Perform the numerical integration
result, error = quad(integrand, a, b)

# Display the result and the error estimate
result, error
