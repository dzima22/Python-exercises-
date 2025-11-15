# Import section
import matplotlib.pyplot as plt
import numpy as np

# Random walk. Trajectory

start = 0
Sn = []
n = 10
move = [-1, 1]
probabilities = [0.5, 0.5]

for i in range(n):
    step = np.random.choice(move, p=probabilities)
    start = start + step
    Sn.append(start)

plt.plot(Sn)
plt.xlabel('Steps', fontsize=20)
plt.ylabel(r'$S_{n}$', fontsize=20)
plt.show()

print(Sn)
