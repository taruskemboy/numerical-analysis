# Gauss-Seidel Iteration Method

# Defining the equations to be solved in diagonally dominant form
# Note: Ensure that the system of equations is diagonally dominant
f1 = lambda x, y, z: (-18 - 2 * y + 3 * z) / 45
f2 = lambda x, y, z: (47 + 3 * x - 2 * z) / 22
f3 = lambda x, y, z: (67 - 5 * x - y) / 20

# Initial guesses for the variables
x0 = 0
y0 = 0
z0 = 0
count = 1

# Reading the tolerable error from the user
e = float(input('Enter tolerable error: '))

# Printing the header for the table of iterations
print('\nCount\tx\ty\tz\n')

# Iteration condition
condition = True

while condition:
    # Calculating the next iteration values
    x1 = f1(x0, y0, z0)
    y1 = f2(x1, y0, z0)
    z1 = f3(x1, y1, z0)
    
    # Printing the current iteration values
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' % (count, x1, y1, z1))
    
    # Calculating the absolute errors
    e1 = abs(x0 - x1)
    e2 = abs(y0 - y1)
    e3 = abs(z0 - z1)
    
    # Preparing for the next iteration
    count += 1
    x0 = x1
    y0 = y1
    z0 = z1
    
    # Checking if the current solution is within the tolerable error
    condition = e1 > e or e2 > e or e3 > e

# Printing the final solution
print('\nSolution: x = %0.3f, y = %0.3f, z = %0.3f\n' % (x1, y1, z1))
