# -*- coding: utf-8 -*-
"""
Example: Consider a set of voltage and current measurements recorded during a 
laboratory session: voltage V[Volts] = [5, 10, 15, 20, 25], 
and current I[Amps] = [1, 2, 3, 4, 5]. Write a Python code to 
calculate the correlation coefficient between V and I, 
using plain Python code.
@author: fglongatt
"""
def calculate_correlation_coefficient(X, Y):
    if len(X) != len(Y):
        raise ValueError("The lists X and Y must have the same length.")
    
    n = len(X)
    
    mean_X = sum(X) / n
    mean_Y = sum(Y) / n
    
    # Calculate the covariance
    covariance = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n))
    
    # Calculate the standard deviations
    std_dev_X = (sum((X[i] - mean_X) ** 2 for i in range(n)) / (n - 1)) ** 0.5
    std_dev_Y = (sum((Y[i] - mean_Y) ** 2 for i in range(n)) / (n - 1)) ** 0.5
    
    # Calculate the correlation coefficient
    correlation_coefficient = covariance / ((n - 1) * std_dev_X * std_dev_Y)
    
    return correlation_coefficient

# Example usage:
# Voltage (in volts)
V = [5, 10, 15, 20, 25]
# Current (in amperes)
I = [1, 2, 3, 4, 5]

correlation_coefficient = calculate_correlation_coefficient(V, I)
print("Correlation coefficient between voltage and current:", correlation_coefficient)
