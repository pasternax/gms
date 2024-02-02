import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('Data/Hark_kr.txt', usecols=(0, 1, 2))
x1, y1, z1 = data1[:, 0], data1[:, 1], data1[:, 2]

data2 = np.loadtxt('Data/Hseyah_kr.txt', usecols=(0, 1, 2))
x2, y2, z2 = data2[:, 0], data2[:, 1], data2[:, 2]

data3 = np.loadtxt('Data/PK1_kr.txt', usecols=(0, 1, 2))
x3, y3, z3 = data3[:, 0], data3[:, 1], data3[:, 2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x1, y1, z1, c='r', marker='o', label='Hark_kr')

ax.scatter(x2, y2, z2, c='g', marker='^', label='Hseyah_kr')

ax.scatter(x3, y3, z3, c='b', marker='s', label='PK1_kr')

ax.legend()
plt.show()
