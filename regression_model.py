import csv
import warnings
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import *
warnings.filterwarnings("ignore")                                  # ignore warnings


# Read the file given and save the data in arrays
def read_CSV(filename, var_title):
	variable = []
	percents = []

	with open(filename, 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			variable.append(row[var_title])
			percents.append(float(row['Percent']))

	return variable, percents


def build_scatter_plot(percents, num_categories, categories):
	plt.figure(figsize=(9,7))

	# Scatter plot for each category
	for x in range(num_categories):
		plt.plot([x]*53, percents[x::num_categories], 'o', label="{0}".format(categories[x]))


def build_regression_plot(percents, num_categories, degrees):
	x_axis = np.arange(num_categories)                             # helper array for categories

	# Get average percents of all categories
	avg_percents = []
	for x in range(num_categories):
		avg_percents.append(sum(percents[x::num_categories]) / 53) # find averages of percents

	# Coorelation Coefficient
	print("R^2 = ", end='')                                        # print R^2
	print(pow(linregress(x_axis, avg_percents)[2],2))              # print coorelation coefficient value

	# Fit and plot the regression line
	fit = sp.polyfit(x_axis, avg_percents, degrees)                # fit the polynomial line to the average of all sets with 3 degrees of freedom
	lin_sp = sp.linspace(0, num_categories-1, 80)                  # smooth out the line by mapping to more points
	plt.plot(lin_sp, sp.polyval(fit,lin_sp), "r-", label="Regression Line")


def display_plot(title, x_label, categories):
	# Labeling and showing the plot
	plt.title("Polynomial Regression\n{0}".format(title))          # set title
	plt.xlabel("{0}".format(x_label))                              # set x label
	plt.ylabel("Asthma Prevalence (percent)")                      # set y label
	labels = categories                                            # label array
	plt.xticks(np.arange(len(categories)))                         # set ticks to replace
	plt.axes().set_xticklabels(labels)                             # replace x-axis with our labels
	plt.legend()                                                   # invoke legend on labels
	plt.show()                                                     # display plot


# Read the CSVs into arrays for ML later
i, p1 = read_CSV('incomeByState.csv', 'Income')
a, p2 = read_CSV('ageByState.csv', 'Age')
r, p3 = read_CSV('raceByState.csv', 'Race')
s, p4 = read_CSV('sexByState.csv', 'Sex')

build_scatter_plot(p1, 5, i[0:5])
build_regression_plot(p1, 5, 3)
display_plot("On Income", "Income Brackets", i[0:5])

build_scatter_plot(p2, 6, a[0:6])
build_regression_plot(p2, 6, 3)
display_plot("On Age", "Age Brackets", a[0:6])

build_scatter_plot(p3, 4, r[0:4])
build_regression_plot(p3, 4, 3)
display_plot("On Race", "Race Brackets", r[0:4])

build_scatter_plot(p4, 2, s[0:2])
build_regression_plot(p4, 2, 3)
display_plot("On Sex", "Sex Brackets", s[0:2])

