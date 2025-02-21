# -*- coding: utf-8 -*-
"""
Example: The leaning tower of Pisa leans and its tilt angle has been increasing 
over time. The table below shows measurements taken from a fixed point on the 
tower and their position if the tower were straight for the years 1975 to 1987. 
Year = [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87] and 
Lean = [642.0, 644.0, 656.0, 667.0, 673.0, 688.0, 696.0, 698.0, 713.0, ...
        717.0, 725.0, 742.0, 757.0]. 
Plot the raw data of the tower leaning over the time.
@author: fglon
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# Given data
years = np.array([75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87])
lean_measurements = np.array([642.0, 644.0, 656.0, 667.0, 673.0, 688.0, 696.0, 698.0, 713.0, 717.0, 725.0, 742.0, 757.0])

# Convert coded measurements to actual lean in meters
lean_meters = 2.9 + (lean_measurements / 10000)

# Plot the raw data
plt.scatter(years, lean_meters, color='blue', label='Observed Data')
plt.xlabel('Year')
plt.ylabel('Lean (meters)')
plt.title('Lean of the Tower of Pisa Over Time')
plt.legend()
plt.grid(True)
plt.show()


#---- MEAN -----------------
mean_valueX = np.mean(years)
print("Mean value Years: X = ", mean_valueX)
mean_valueY = np.mean(lean_meters)
print("Mean value lean_measurements: Y=", mean_valueY)
#---- CORRELATION -----------------
correlation_matrix = np.corrcoef(years, lean_meters)
correlation_coefficient = correlation_matrix[0, 1]
print(f"Correlation Coefficient: rXY =  {correlation_coefficient}")
#---- COVARIANCE 
covariance_matrix = np.cov(years, lean_meters)
covariance = covariance_matrix[0, 1]
print("Covariance between X and Y: cov(X,Y) =", covariance)
variance_sample = np.var(years, ddof=1)  # Sample variance
# Calculate standard deviation
std_deviation_sample = np.std(years, ddof=1)  # Sample standard deviation
print(f"Sample Variance: {variance_sample}")
print(f"Sample Standard Deviation: {std_deviation_sample}")

beta1 = covariance/variance_sample
print(f"Beta1: {beta1}")
beta0 = mean_valueY  - beta1*mean_valueX 
print(f"Beta0: {beta0}")


