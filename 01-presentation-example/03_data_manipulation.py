
import csv
from datetime import datetime

filename = r'data\WMT_US.csv'

with open(filename, 'r') as f:
    rows = csv.reader(f)

    # skip header row
    header = next(f)

    for row in rows:
        row[2] = datetime.strptime(row[2], "%m/%d/%Y")

        # convert string to integer
        row[3] = int(row[3])
        row[4] = int(row[4])



