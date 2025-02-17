# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:56:45 2025

@author: fglon
"""

import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.random.normal(0, 1, 1000)  # Generate 1000 random numbers from a normal distribution

# Create histogram
plt.hist(data, bins=30, color='skyblue', edgecolor='black')

# Add title and labels
plt.title('Histogram of Randomly Generated Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show plot
plt.tight_layout()
plt.show()
