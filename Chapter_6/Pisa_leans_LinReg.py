# -*- coding: utf-8 -*-
"""
Example: The leaning tower of Pisa leans and its tilt angle has been increasing 
over time. The table below shows measurements taken from a fixed point on the 
tower and their position if the tower were straight for the years 1975 to 1987. 
Year = [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87] and 
Lean = [642.0, 644.0, 656.0, 667.0, 673.0, 688.0, 696.0, 698.0, 713.0, ...
        717.0, 725.0, 742.0, 757.0]. 
Create the linear regresion model
@author: fglongatt
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# Given data
years = np.array([75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87])
lean_measurements = np.array([642.0, 644.0, 656.0, 667.0, 673.0, 688.0, 696.0, 698.0, 713.0, 717.0, 725.0, 742.0, 757.0])
# Convert coded measurements to actual lean in meters
lean_meters = 2.9 + (lean_measurements / 10000)
# Fit the linear regression model
years_reshaped = years.reshape(-1, 1)
model = LinearRegression().fit(years_reshaped,lean_meters)
slope = model.coef_[0]
intercept = model.intercept_
print(f"Linear Regression Coefficients:\nIntercept: {intercept:.4f} meters\nSlope: {slope:.4f} meters/year")
# Plot the data and the linear regression line
plt.scatter(years, lean_meters, color='blue', label='Observed Data')
plt.plot(years, model.predict(years_reshaped), color='red', label='Regression Line')
plt.xlabel('Year')
plt.ylabel('Lean (meters)')
plt.title('Lean of the Tower of Pisa Over Time')
plt.legend()
plt.grid(True)
plt.show()
