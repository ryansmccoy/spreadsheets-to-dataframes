
import csv
from datetime import datetime
from pprint import pprint

filename = r'data\WMT_US.csv'

records = []

with open(filename, 'r') as f:
    rows = csv.reader(f)

    # skip header row
    header = next(f)

    for row in rows:
        row[2] = datetime.strptime(row[2], "%m/%d/%Y")
        row[3] = int(row[3])
        row[4] = int(row[4])
        # perform calculation
        profit = row[3] - row[4]

        record = {
            "ticker": row[0],
            "name": row[1],
            "date": row[2],
            "sales": row[3],
            "expenses": row[4],
            "profit": profit
        }

        records.append(record)

pprint(records)
