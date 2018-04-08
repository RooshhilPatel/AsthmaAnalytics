import pandas as pd
import matplotlib.pyplot as plt
import csv


# Read the file given and save the data in arrays
def readCSV(filename, var_title, states=[]):
    variable = []
    percents = []

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            states.append(row['State'])
            variable.append(row[var_title])
            percents.append(round((float(row['Percent']) / 100), 3))

    return states, variable, percents


# read the csvs into arrays for ML later
s, r, p1 = readCSV('raceByState.csv', 'Race')
s, s, p2 = readCSV('sexByState.csv', 'Sex')
s, i, p3 = readCSV('incomeByState.csv', 'Income')
s, a, p4 = readCSV('ageByState.csv', 'Age')

income_columns = list(set(i))
first_range = p3[0::5]
second_range = p3[1::5]
third_range = p3[2::5]
fourth_range = p3[3::5]
fifth_range = p3[4::5]
inc = pd.DataFrame(list(zip(first_range,second_range,third_range,fourth_range,fifth_range)))
inc = inc.values.tolist()

for x in range(5):
	plt.plot([x]*53, p3[x::5], 'o')

plt.xticks([0, 1, 2, 3, 4])
plt.axes().set_xticklabels(income_columns)
plt.show()
