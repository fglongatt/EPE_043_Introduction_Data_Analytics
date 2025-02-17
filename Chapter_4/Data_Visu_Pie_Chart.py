# -*- coding: utf-8 -*-
"""
Example: Create a pie chart category data Group1 = [1, 1.7, 7]. 
Write a Python code to create the bar plot using matplotlib
@author: fglongatt
"""
import matplotlib.pyplot as plt
# Data
data = [1, 1.7, 7]
labels = ['Category 1', 'Category 2', 'Category 3']
colors = ['#ff9999','#66b3ff','#99ff99']
# Create pie chart
plt.pie(data, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
# Add title
plt.title('Pie Chart of Given Data')
# Show plot
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
plt.tight_layout()
plt.show()