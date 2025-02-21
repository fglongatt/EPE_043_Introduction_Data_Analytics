# -*- coding: utf-8 -*-
"""
Example: Consider a set of voltage and current measurements recorded 
during a laboratory session: voltage V[Volts] = [5, 10, 15, 20, 25], 
nd current I[Amps] = [1, 2, 3, 4, 5]. Write a 
Python code to calculate the covariance between V and I, 
using plain NumPy.
@author: fglongatt
"""
import numpy as np
# Voltage and current measurements
# Voltage (in volts)
voltage = np.array([5, 10, 15, 20, 25])
# Current (in amperes)
current = np.array([1, 2, 3, 4, 5])
# Calculate covariance
covariance_matrix = np.cov(voltage, current)
covariance_VI = covariance_matrix[0, 1]
print("Covariance between voltage and current:", covariance_VI)