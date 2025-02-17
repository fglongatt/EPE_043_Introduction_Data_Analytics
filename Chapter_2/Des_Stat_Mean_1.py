# -*- coding: utf-8 -*-
"""
Example: Descriptive Statistics
Created on Mon Feb 17 13:12:43 2025
@author: fglongatt

Example: Consider the dataset S ={ 5, 8, 12, 7}. 
Write a Python code to calculate the mean value 
of a dataset S using plain and basic Python code.

"""
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# Usage
numbers = [5, 8, 12,7]
mean_value = calculate_mean(numbers)
print(f"The mean value is: {mean_value}")
