'''Assume you throw darts at a square box. Now assume that there is a circle in the square who's origin is the
center of the square and has diameter which is the same length as the squares side. Using the number of darts that land
in the circle versus the square we can estimate pi'''

import numpy as np
import random as random
import matplotlib.pyplot as plt


n = 5000 #Number of shots
r = 100 #Radius
h = r #x value for center of a circle
k = r #y value for center of a circle
grid = []


def darts(grid, n, r):
    for num in range(0, n):
        point = []
        for num in range(0, 2):
            point.append(random.randrange(0, 2 * r))

        grid.append(point)

    return (grid)

def pi_estimate(r, h, k, points):
    rect_count = 0
    circ_count = 0

    x_in = []
    y_in = []
    x_out = []
    y_out = []

    for point in points:
        rt = ((point[0] - h) ** 2) + ((point[1] - k) ** 2)
        if rt < r ** 2 or rt == r ** 2:
            circ_count += 1
            rect_count += 1
            x_in.append(point[0])
            y_in.append(point[1])

        else:
            rect_count += 1
            x_out.append(point[0])
            y_out.append(point[1])

    est_pi = (circ_count / rect_count) * 4

    plt.scatter(x_in, y_in)
    plt.scatter(x_out, y_out)
    plt.title("Darts Distribution within the grid")
    plt.show()

    print("Darts in Rectangle:", rect_count)
    print("Darts in Circle:", circ_count)
    print("Simulated Pi is:", est_pi)


points = darts(grid, n, r)
pi_estimate(r, h, k, points)