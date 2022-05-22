# Python program for JSON to CSV conversion

import json
import csv

# Opening the json file and loading the data 
# into the variable data
with open('names.json') as json_file:
    names = json.load(json_file)

names_data = names['names']

# Opens a file for writing
data_file = open('data_file.csv', 'w')

# Creates the csv_writer object
csv_writer = csv.writer(data_file)

# Counter for the headers
count = 0

for name in names:
    if count == 0:

        # Writes the headers for the csv file
        header = name.keys()
        csv_writer.writerow(header)
        count += 1

    # Writes the data
    csv_writer.writerow(name.values())

data_file.close()