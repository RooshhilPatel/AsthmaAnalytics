from requests import get
from bs4 import BeautifulSoup
import csv


# ##############METHODS################# #
# write and export data to csv
def export_to_csv(csv_name, variable, data):
    with open(csv_name, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerow(["State", variable, "Percent"])
        writer.writerows(data)


# write and export data to csv
def export_to_state_csv(csv_name, data):
    with open(csv_name, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerow(["State", "Percent"])
        writer.writerows(data)


# split data to keep only state information (state rows)
def filter_states(data):
    state_data = []
    for d in data:
        if d and len(d[0]) == 2:
            state_data.append(d)
    return state_data


# converts tags(<tr>) to list of list and removes extra columns and data
def replace_useless_stuff(rows):
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols if ele]  # get rid of empty values
        if cols:
            data.append(cols[:4])                         # only first 4 columns
    for d in data:                                        # drop 3rd column (size) because we only want percent
        del d[2]
    data = filter_states(data)                            # filter non states
    return data


# converts tags(<tr>) to list of list and removes extra columns and data
# special replace method because different format
def replace_useless_sex_stuff(rows):
    data = []
    data2 = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols if ele]  # get rid of empty values
        if cols:
            data.append(cols[:8])                         # up to the female percent column
    data = filter_states(data)                            # filter non states
    for d in data:                                        # delete extra columns and change format
        del d[6]
        del d[5]
        del d[4]
        del d[3]
        del d[1]
        data2.append([d[0], "Male", d[1]])
        data2.append([d[0], "Female", d[2]])
    del data
    return data2


def replace_useless_state_stuff(rows):
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols if ele]  # get rid of empty values
        if cols:
            data.append(cols[:3])                         # only first 3 columns
    for d in data:                                        # drop 2rd column (size) because we only want percent
        del d[1]
    data = filter_states(data)                            # filter non states
    return data


# does the scraping and filters extra data
def scrape_data(content):
    # Find strong tags and table rows in the table
    table_rows = content.find("div", id="contentArea").find("table").findAll("tr")  # rawData
    table_data = replace_useless_stuff(table_rows)  # preprocessedData
    return table_data


# does the scraping and filters extra data for sex content
# special scrape method to call the replace method for sex content
def scrape_sex_data(content):
    # Find strong tags and table rows in the table
    table_rows = content.find("div", id="contentArea").find("table").findAll("tr")  # rawData
    table_data = replace_useless_sex_stuff(table_rows)  # preprocessedData
    return table_data


# does the scraping and filters extra data for state content
# special scrape method to call the replace method for state content
def scrape_state_data(content):
    # Find strong tags and table rows in the table
    table_rows = content.find("div", id="contentArea").find("table").findAll("tr")  # rawData
    table_data = replace_useless_state_stuff(table_rows)  # preprocessedData
    return table_data


# ##############MAIN PROGRAM################ #
# get the website and the HTML in lxml format
race_page = get("https://www.cdc.gov/asthma/brfss/2014/tableL4.htm")
income_page = get("https://www.cdc.gov/asthma/brfss/2014/tablel7.htm")
age_page = get("https://www.cdc.gov/asthma/brfss/2014/tableL3.htm")
sex_page = get("https://www.cdc.gov/asthma/brfss/2014/tableL21.htm")
state_page = get("https://www.cdc.gov/asthma/brfss/2014/tableL1.htm")
race_content = BeautifulSoup(race_page.content, "lxml")
income_content = BeautifulSoup(income_page.content, "lxml")
age_content = BeautifulSoup(age_page.content, "lxml")
sex_content = BeautifulSoup(sex_page.content, "lxml")
state_content = BeautifulSoup(state_page.content, "lxml")

# scrape the content and filter to get useful data (Preprocess Data)
race_data = scrape_data(race_content)
income_data = scrape_data(income_content)
age_data = scrape_data(age_content)
sex_data = scrape_sex_data(sex_content)
state_data = scrape_state_data(state_content)

# Export to respective CSV files
export_to_csv("raceByState.csv", "Race", race_data)
export_to_csv("incomeByState.csv", "Income", income_data)
export_to_csv("ageByState.csv", "Age", age_data)
export_to_csv("sexByState.csv", "Sex", sex_data)
export_to_state_csv("prevalenceByState.csv", state_data)