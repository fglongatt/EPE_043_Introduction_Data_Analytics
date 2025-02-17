# -*- coding: utf-8 -*-
"""
Example: Descriptive Statistics
Created on Mon Feb 17 13:12:43 2025
@author: fglongatt

Example: Consider the dataset S ={ 5, 8, 12, 7}. 
Write a Python code to calculate the mode value 
of a dataset S using NumPy code.
"""
import numpy as np
from scipy import stats
# Define the data set
data = [5, 8, 12, 7]

# Calculate the mode using SciPy
mode = stats.mode(data)

print("Mode:", mode.mode[0])
print("Frequency of the mode:", mode.count[0])