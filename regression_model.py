import csv
import warnings
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import *
warnings.filterwarnings("ignore")                                       # ignore warnings


# Read the file given and save the data in arrays
def readCSV(filename, var_title):
	states = []
	variable = []
	percents = []

	with open(filename, 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			states.append(row['State'])
			variable.append(row[var_title])
			percents.append(float(row['Percent']))

	return states, variable, percents


# Read the CSVs into arrays for ML later
s, i, p1 = readCSV('incomeByState.csv', 'Income')                       # read csv file into the respective variables
# s, r, p2 = readCSV('raceByState.csv', 'Race')
# s, s, p3 = readCSV('sexByState.csv', 'Sex')
# s, a, p4 = readCSV('ageByState.csv', 'Age')

x_axis = np.array([0, 1, 2, 3, 4])                                      # helper array for categories
plt.figure(figsize=(9,7))

# Scatter plot for each category
for x in range(5):
	plt.plot([x]*53, p1[x::5], 'o', label="Income Bracket %d" % (x+1))  # plot the points as circles

# Get average percents of all categories
avg_percents = []
for j in range(5):
	avg_percents.append(sum(p1[j::5]) / 53)                             # find averages

# Fit and plot the regression line
fit = sp.polyfit(x_axis, avg_percents, 3)                               # fit the polynomial line to the average of all sets with 3 degrees of freedom
lin_sp = sp.linspace(0, 4, 80)                                          # smooth out the line by mapping to more points
plt.plot(lin_sp, sp.polyval(fit,lin_sp), "r-", label="Regression Line") # plot a red regression line

# Coorelation Coefficient
print("R^2 = ", end='')                                                 # print R^2
print(pow(linregress(x_axis, avg_percents)[2],2))                       # print coorelation coefficient value

# Labeling and showing the plot
plt.title("Polynomial Regression\non Income")                           # set title
plt.xlabel("Income Brackets")                                           # set x label
plt.ylabel("Asthma Prevalence (percent)")                               # set y label
plt.legend()                                                            # invoke legend on labels
income_columns = list(set(i))                                           # label array
plt.xticks(x_axis)                                                      # set ticks to replace
plt.axes().set_xticklabels(income_columns)                              # replace x-axis with our labels
plt.show()                                                              # display plot
