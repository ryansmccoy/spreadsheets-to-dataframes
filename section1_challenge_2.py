# Perform an Excel VLOOKUP with a Python Dictionary

# Challenge 2
# Modify the code below to sum up all the donations by the companies in the list

import csv
import os
from pprint import pprint

current_directory = os.getcwd()

pycon_sponsors_filename = 'pycon_sponsors.csv'
pycon_sponsors_filepath = os.path.join(current_directory, "data", pycon_sponsors_filename)

# print(pycon_sponsors_filepath)

sponsor_levels = [{'sponsor_level': 'VISIONARY', 'amount': 150000},
                 {'sponsor_level': 'SUSTAINABILITY', 'amount': 90000},
                 {'sponsor_level': 'MAINTAINING', 'amount': 60000},
                 {'sponsor_level': 'CONTRIBUTING', 'amount': 30000},
                 {'sponsor_level': 'SUPPORTING', 'amount': 15000},
                 {'sponsor_level': 'PARTNER', 'amount': 7500},
                 {'sponsor_level': 'PARTICIPATING', 'amount': 3750},
                 {'sponsor_level': 'ASSOCIATE', 'amount': 1500}]

sponsor_vlookup = {}

for sponsor_level in sponsor_levels:
    sponsor_vlookup[sponsor_level['sponsor_level']] = sponsor_level['amount']

pprint(sponsor_levels)

pycon_sum = []

# print(pycon_sponsors_filepath)

with open(pycon_sponsors_filepath, 'r') as f:
    rows = csv.reader(f)

    header = next(f)

    for row_number, row in enumerate(rows):
        ticker, name, level = row
        print("Company Number:\t", row_number, "\n\tDCompany:", name, "\n\tLevel: ",level, "\n\tDonated:", sponsor_vlookup[row[2]], "\n")

"""
Current Output:

[{'amount': 150000, 'sponsor_level': 'VISIONARY'},
 {'amount': 90000, 'sponsor_level': 'SUSTAINABILITY'},
 {'amount': 60000, 'sponsor_level': 'MAINTAINING'},
 {'amount': 30000, 'sponsor_level': 'CONTRIBUTING'},
 {'amount': 15000, 'sponsor_level': 'SUPPORTING'},
 {'amount': 7500, 'sponsor_level': 'PARTNER'},
 {'amount': 3750, 'sponsor_level': 'PARTICIPATING'},
 {'amount': 1500, 'sponsor_level': 'ASSOCIATE'}]

Company Number:	 0 
	DCompany: ALPHABET INC. 
	Level:  VISIONARY 
	Donated: 150000 
Company Number:	 1 
	DCompany: AMAZON COM INC 
	Level:  SUSTAINABILITY 
	Donated: 90000 
Company Number:	 2 
	DCompany: BLOOMBERG 
	Level:  VISIONARY 
	Donated: 150000 
Company Number:	 3 
	DCompany: CAPITAL ONE FINANCIAL CORP 
	Level:  MAINTAINING 
	Donated: 60000 
Company Number:	 4 
	DCompany: CORNING INC 
	Level:  MAINTAINING 
	Donated: 60000 
Company Number:	 5 
	DCompany: ELASTIC N.V. 
	Level:  PARTNER 
	Donated: 7500 
Company Number:	 6 
	DCompany: FACEBOOK INC 
	Level:  SUSTAINABILITY 
	Donated: 90000 
Company Number:	 7 
	DCompany: HUAWEI TECHNOLOGIES 
	Level:  SUSTAINABILITY 
	Donated: 90000 
Company Number:	 8 
	DCompany: INTERNATIONAL BUSINESS MACHINES CORP 
	Level:  CONTRIBUTING 
	Donated: 30000 
Company Number:	 9 
	DCompany: JPMORGAN CHASE & CO 
	Level:  SUPPORTING 
	Donated: 15000 
Company Number:	 10 
	DCompany: MICROSOFT CORP 
	Level:  VISIONARY 
	Donated: 150000 
Company Number:	 11 
	DCompany: NETFLIX INC 
	Level:  PARTNER 
	Donated: 7500 
Company Number:	 12 
	DCompany: SALESFORCE.COM INC. 
	Level:  SUSTAINABILITY 
	Donated: 90000 
Company Number:	 13 
	DCompany: SLACK TECHNOLOGIES INC. 
	Level:  MAINTAINING 
	Donated: 60000 

"""
"""
Expected Output:

Total Sum: 1050000

"""
