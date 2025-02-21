# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 13:10:12 2025

@author: fglon
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mu = 8  # Mean
sigma = 8  # Standard deviation
alpha = 0.05  # Significance level

# Generate x values
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

# Generate y values for normal distribution
y = norm.pdf(x, mu, sigma)

# Critical values for 5% significance level (two-tailed)
z_critical = norm.ppf(1 - alpha / 2)
lower_critical_value = mu - z_critical * sigma
upper_critical_value = mu + z_critical * sigma

# Plot the normal distribution
plt.plot(x, y, label='Normal Distribution', color='blue')

# Fill the critical regions
plt.fill_between(x, y, where=(x <= lower_critical_value), color='red', alpha=0.5, label='Critical Region')
plt.fill_between(x, y, where=(x >= upper_critical_value), color='red', alpha=0.5)

# Add lines for critical values
plt.axvline(lower_critical_value, color='red', linestyle='--', label=f'Lower Critical Value ({lower_critical_value:.2f})')
plt.axvline(upper_critical_value, color='red', linestyle='--', label=f'Upper Critical Value ({upper_critical_value:.2f})')

# Customize plot
plt.title('Normal Distribution with Critical Regions')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()

# Show plot
plt.show()
