# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:18:56 2025

@author: fglon
"""

import random
import matplotlib.pyplot as plt

def estimate_pi(num_samples):
    inside_circle = 0
    pi_values = []
    points_x_inside, points_y_inside = [], []
    points_x_outside, points_y_outside = [], []
    
    for i in range(1, num_samples + 1):
        x, y = random.uniform(0, 1), random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
            points_x_inside.append(x)
            points_y_inside.append(y)
        else:
            points_x_outside.append(x)
            points_y_outside.append(y)
        pi_estimate = (inside_circle / i) * 4
        pi_values.append(pi_estimate)
    
    return pi_values, points_x_inside, points_y_inside, points_x_outside, points_y_outside

# Parameters
num_samples = 10000
pi_values, points_x_inside, points_y_inside, points_x_outside, points_y_outside = estimate_pi(num_samples)

# Plotting the points and the estimated value of π
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plotting the quarter circle points
ax[0].scatter(points_x_inside, points_y_inside, color='blue', s=1, label='Inside Quarter Circle')
ax[0].scatter(points_x_outside, points_y_outside, color='red', s=1, label='Outside Quarter Circle')
ax[0].set_aspect('equal')
ax[0].set_title('Monte Carlo Simulation (Quarter Circle)')
ax[0].legend()
ax[0].grid(True)

# Plotting the estimation of π
ax[1].plot(range(1, num_samples + 1), pi_values, label='Estimated π')
ax[1].axhline(y=3.141592653589793, color='r', linestyle='-', label='Actual π')
ax[1].set_xlabel('Number of Samples')
ax[1].set_ylabel('Estimated Value of π')
ax[1].set_title('Monte Carlo Estimation of π')
ax[1].legend()
ax[1].grid(True)

plt.show()

