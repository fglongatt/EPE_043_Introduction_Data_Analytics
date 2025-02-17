# -*- coding: utf-8 -*-
"""
Example: Descriptive Statistics
Created on Mon Feb 17 13:12:43 2025
@author: fglongatt

Example: Consider the dataset S ={ 5, 8, 12, 7}. 
Write a Python code to calculate the mean value 
of a dataset S  using NumPy code.
"""

import numpy as np
# Create a dataset in the form of an array
# numpy.array: Creates an array
data = np.array([5, 8, 12,7])
# Calculate the mean value
# numpy.mean: Compute the arithmetic mean along the specified axis.
mean_value = np.mean(data)
print("Mean value:", mean_value)
