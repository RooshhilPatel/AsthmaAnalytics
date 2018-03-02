from requests import get
from bs4 import BeautifulSoup
import csv

###############METHODS##################
#prints all items from given list if not empty
def printAllItems(givenList):
    for item in givenList:
        if item:
            print(item)
    return

#split data to keep only state information
def splitData(data):
    stateData = []
    for d in data:
        if d and len(d[0]) == 2:
            stateData.append(d)
    return stateData

#converts tags to list of list and removes extra columns and data
def replaceUselessStuff(rows):
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols if ele] # Get rid of empty values
        data.append(cols[:4])                            #only first 4 columns
    data = splitData(data)
    return data

#does the scraping and filters extra data
def scrapeData():
    #Find strong tags and table rows in the table
    TableRows = stuff.find("div", id="contentArea").find("table").findAll("tr") #rawData
    TableData = replaceUselessStuff(TableRows)                                  #preprocessedData
    return TableData

###############MAIN PROGRAM#################
#get the website and the HTML in lxml format
page = get("https://www.cdc.gov/asthma/brfss/2014/tableL4.htm")
stuff = BeautifulSoup(page.content, "lxml")
data = scrapeData()
# printAllItems(data)

#Export to CSV file
with open("test.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(["State","Race","Size","Percent"])
    writer.writerows(data)
