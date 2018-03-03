from requests import get
from bs4 import BeautifulSoup
import csv

###############METHODS##################
#prints all items from given list if item is not empty
def printAllItems(givenList):
    for item in givenList:
        if item:
            print(item)
    return

#split data to keep only state information (state rows)
def filterStates(data):
    stateData = []
    for d in data:
        if d and len(d[0]) == 2:
            stateData.append(d)
    return stateData

#converts tags(<tr>) to list of list and removes extra columns and data
def replaceUselessStuff(rows):
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols if ele] #get rid of empty values
        if cols:
            data.append(cols[:4])                        #only first 4 columns
    for d in data:                                       #drop 3rd column (size) because we only want percent
        del d[2]
    data = filterStates(data)
    return data

#converts tags(<tr>) to list of list and removes extra columns and data
#special replace method because different format
def replaceUselessSexStuff(rows):
    data = []
    data2 = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols if ele] #get rid of empty values
        if cols:
            data.append(cols[:8])                        #up to the female percent column
    data = filterStates(data)                            #filter non states
    for d in data:                                       #delete extra columns and change format
        del d[6]
        del d[5]
        del d[4]
        del d[3]
        del d[1]
        data2.append([d[0],"male",d[1]])
        data2.append([d[0],"female",d[2]])
    del data
    return data2

#does the scraping and filters extra data
def scrapeData(content):
    #Find strong tags and table rows in the table
    TableRows = content.find("div", id="contentArea").find("table").findAll("tr") #rawData
    TableData = replaceUselessStuff(TableRows)                                    #preprocessedData
    return TableData

#does the scraping and filters extra data for sex content
#special scrape method to call the replace method for sex content
def scrapeSexData(content):
    #Find strong tags and table rows in the table
    TableRows = content.find("div", id="contentArea").find("table").findAll("tr") #rawData
    TableData = replaceUselessSexStuff(TableRows)                                 #preprocessedData
    return TableData

###############MAIN PROGRAM#################
#get the website and the HTML in lxml format
race_page = get("https://www.cdc.gov/asthma/brfss/2014/tableL4.htm")
income_page = get("https://www.cdc.gov/asthma/brfss/2014/tablel7.htm")
age_page = get("https://www.cdc.gov/asthma/brfss/2014/tableL3.htm")
sex_page = get("https://www.cdc.gov/asthma/brfss/2014/tableL21.htm")
race_content = BeautifulSoup(race_page.content, "lxml")
income_content = BeautifulSoup(income_page.content, "lxml")
age_contnet = BeautifulSoup(age_page.content, "lxml")
sex_content = BeautifulSoup(sex_page.content, "lxml")

#scrape the content and filter to get useful data (Preprocess Data)
race_data = scrapeData(race_content)
income_data = scrapeData(income_content)
age_data = scrapeData(age_contnet)
sex_data = scrapeSexData(sex_content)
# printAllItems(sex_data)

#Export to respective CSV files
with open("raceByState.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(["State","Race","Percent"])
    writer.writerows(race_data)
with open("incomeByState.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(["State","Income","Percent"])
    writer.writerows(income_data)
with open("ageByState.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(["State","Age","Percent"])
    writer.writerows(age_data)
with open("sexByState.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(["State","Sex","Percent"])
    writer.writerows(sex_data)
