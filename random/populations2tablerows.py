''' populations2tablerows.py

    A script for converting the city data in "Baltimore,14,26,47..." form into
    rows that match the populations table structure "Baltimore,1790,14",
    "Baltimore,1800,26", etc.
'''

import sys
import csv

reader = csv.reader(sys.stdin)
writer = csv.writer(sys.stdout)

headingRow = reader.next()[1:]

cities = {}
for row in reader:
    row = map(str.strip, row)
    assert len(row) == len(headingRow) + 1
    cities[row[0]] = row[1:]

for city in cities:
    for k in range(len(headingRow)):
        cityRow = cities[city]
        yearString = headingRow[k]
        populationString = cityRow[k].replace(',', '') # if the CSV numbers have commas in them, delete them
        if populationString == '':
            populationString = '0'
        writer.writerow([city, yearString, populationString])
