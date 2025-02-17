# -*- coding: utf-8 -*-
"""
Example: Descriptive Statistics
Created on Mon Feb 17 13:12:43 2025
@author: fglongatt

Example: Consider the dataset S ={ 5, 8, 12, 7}. 
Write a Python code to calculate the variance and the standard deviation 
of a dataset S using NumPy code.
"""
import numpy as np
# Define the data set
data = [5, 8, 12, 7]
# Calculate variance
variance = np.var(data, ddof=0)  # Population variance
variance_sample = np.var(data, ddof=1)  # Sample variance
# Calculate standard deviation
std_deviation = np.std(data, ddof=0)  # Population standard deviation
std_deviation_sample = np.std(data, ddof=1)  # Sample standard deviation

print(f"Population Variance: {variance}")
print(f"Sample Variance: {variance_sample}")
print(f"Population Standard Deviation: {std_deviation}")
print(f"Sample Standard Deviation: {std_deviation_sample}")