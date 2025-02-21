# -*- coding: utf-8 -*-
"""
Example: Consider a set of voltage and current measurements recorded during a 
laboratory session: voltage V[Volts] = [5, 10, 15, 20, 25], 
and current I[Amps] = [1, 2, 3, 4, 5]. 
Write a Python code to calculate the correlation coefficient between V and I, 
using plain NumPy.
@author: fglongatt
"""
import numpy as np
# Given data
V = np.array([5, 10, 15, 20, 25])
I = np.array([1, 2, 3, 4, 5])

# Compute the correlation coefficient
correlation_matrix = np.corrcoef(V, I)
correlation_coefficient = correlation_matrix[0, 1]
print(f"Correlation Coefficient: {correlation_coefficient}")

