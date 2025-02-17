# -*- coding: utf-8 -*-
"""
Example: Create a scatter plot of the data represented by 
x = [1, 2, 3, 4, 5], y = [2, 4, 1, 8, 7]. 
Write a Python code to create a scatter plot 
for the data using matplotlib.

@author: fglongatt
"""
import matplotlib.pyplot as plt
# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]
# Create scatter plot
plt.scatter(x, y, color='blue', marker='o')
# Add title and labels
plt.title('Scatter Plot of Given Data')
plt.xlabel('X values')
plt.ylabel('Y values')
# Show plot
plt.tight_layout()
plt.show()