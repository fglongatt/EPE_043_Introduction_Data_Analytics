# -*- coding: utf-8 -*-
"""
Example: Consider a set of voltage and current measurements recorded during a 
laboratory session: voltage 
V[Volts] = [5, 10, 15, 20, 25], and current I[Amps] = [1, 2, 3, 4, 5]. 
Write a Python code to calculate the covariance between V and I, 
using plain Python code.
@author: fglongatt
"""
# Define a function names Calculate_Covariance
def calculate_covariance(X, Y):
    if len(X) != len(Y):
        raise ValueError("The lists X and Y must have the same length.")
    n = len(X)
    mean_X = sum(X) / n
    mean_Y = sum(Y) / n
    
    covariance = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n)) / (n - 1)
    return covariance

# Example usage:
# Voltage (in volts)
voltage = [5, 10, 15, 20, 25]
# Current (in amperes)
current = [1, 2, 3, 4, 5]

covariance_VI = calculate_covariance(voltage, current)
print("Covariance between voltage and current:", covariance_VI)
