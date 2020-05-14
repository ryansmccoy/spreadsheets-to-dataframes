
import csv
from datetime import datetime

filename = r'00-data\WMT_US.csv'

with open(filename, 'r') as f:
    rows = csv.reader(f)

    # skip header row
    header = next(f)

    for row in rows:
        print(row)
        row[0] = row[0].strip('"')
        row[1] = row[1].strip('"')
        row[2] = datetime.strptime(row[2], "%m/%d/%Y")
        row[3] = int(row[3])
        row[4] = int(row[4])



