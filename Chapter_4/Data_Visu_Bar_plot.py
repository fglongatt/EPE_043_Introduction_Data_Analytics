# -*- coding: utf-8 -*-
"""
Example: Create a bar plot for three category data Group1 = [1, 1.5, 7], 
Group2 = [2, 2.3, 4], Group3 = [9, 4, 5]. Write a python code to create the bar 
plot using matplotlib
  
Created on Mon Feb 17 19:13:49 2025

@author: fglongatt
"""

import numpy as np 
import matplotlib.pyplot as plt 

barWidth = 0.25
fig = plt.subplots(figsize =(12, 8)) 
# plt.subplots: Creates a figure and a grid of subplots with a single call
# Create a dataset 
Group1 = [1, 1.5, 7] 
Group2 = [2, 2.3, 4] 
Group3 = [9, 4, 5] 

br1 = np.arange(len(Group1)) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 
# matplotlib.pyplot.bar: The bars are positioned at x with the given alignment. 
# Their dimensions are given by height and width. The vertical 
# baseline is bottom (default 0).
plt.bar(br1, Group1, color ='r', width = barWidth, 
        edgecolor ='grey', label ='Group 1') 
plt.bar(br2, Group2, color ='g', width = barWidth, 
        edgecolor ='grey', label ='Group 2') 
plt.bar(br3, Group3, color ='b', width = barWidth, 
        edgecolor ='grey', label ='Group 3')
plt.xlabel('Category', fontweight ='bold', fontsize = 15) 
plt.ylabel('Value', fontweight ='bold', fontsize = 15) 
plt.xticks([r + barWidth for r in range(len(Group1))], 
        ['Category 1', 'Category 2', 'Category 3'])
plt.legend()
plt.show() 