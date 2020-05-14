
import csv

filename = r'00-data\WMT_US.csv'

total = 0.0

with open(filename, 'r') as f:
    rows = csv.reader(f)

    # skip header row
    header = next(f)

    for row in rows:
        print(row)

