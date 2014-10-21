''' cities2postgresql.py

    A script for converting some city population data into SQL for use in PostgreSQL.
    Call this via "python cities2postgresql.py < populations.csv" where populations.csv
    has the following structure:

    * One heading row at the top: "Cities,1790,1800,..." (i.e. a heading for the first
      column, followed by a year at the top of each successive column).
    * Each row after that is of the form "Baltimore,14,26,47,..." where the numbers are
      city population in thousands for each of the years in the heading row.
    * No duplicate city names.

    This is one of those quick scripts that you write for a specific purpose and then
    discard. It's not generalized in any way, and there are definitely better ways
    to do this.
'''

import sys
import csv

# Set up the CSV reader object to read from standard input and skip the title row.
reader = csv.reader(sys.stdin)
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
        query = "INSERT INTO populations (city, year, population)"
        query +=   " VALUES ('%s', %s, %s);" % (city, yearString, populationString)
        print query
