from sklearn import svm
import numpy as np
import csv


#Read the file given and save the data in arrays
def readCSV(filename, var_title):
    states = []
    variable = []
    percents = []

    with open(filename,'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            states.append(row['State'])
            variable.append(row[var_title])
            percents.append(row['Percent'])

    return states, variable, percents


#read the csvs into arrays for ML later
s1, r, p1 = readCSV('raceByState.csv', 'Race')
s2, s, p2 = readCSV('sexByState.csv', 'Sex')
s3, i, p3 = readCSV('incomeByState.csv', 'Income')
s4, a, p4 = readCSV('ageByState.csv', 'Age')
