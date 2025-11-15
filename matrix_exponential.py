# Define the generator matrix X (replace with your actual data)
from scipy.linalg import expm
import matplotlib.pyplot as plt
import numpy as np
X = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.208452313, 0, -0.416904626, 0.208452313, 0, 0, 0, 0, 0],
    [0, 0, 0.412895928, -0.412895928, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -0.224684518, 0.224684518, 0, 0, 0],
    [0, 0, 0, 0, 0, -0.407639044, 0.407639044, 0, 0],
    [0, 0, 0, 0, 0, 0.285007808, -0.380010411, 0.095002603, 0],
    [0, 0, 0, 0, 0, 0, 1.051873199, -2.103746398, 1.051873199],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    
])




def matrix_exponential(X):
    identity_matrix = np.eye(X.shape[0])
    k= -1*X.flat[np.abs(X).argmax()]
    scaled_X = X / (k+.5)
    print(k)
    matrix_power = np.add(identity_matrix , scaled_X)
    return matrix_power
# Compute the matrix exponential
result_matrix = matrix_exponential(X)

# Print the result (you can adjust the precision as needed)
np.set_printoptions(precision=6, suppress=True)
print("Matrix Exponential:")
#print(result_matrix)

for row in result_matrix:
    print(" ".join(f"{val:.6f}" for val in row))





