
import csv

filename = r'data\WMT_US.csv'

total = 0.0

with open(filename, 'r') as f:
    rows = csv.reader(f)

    # save header row
    header = next(f)
    # and skip to next row

    for row in rows:
        print(row)

