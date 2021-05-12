# Perform an Excel VLOOKUP with a Python Dictionary

# Challenge 1
# Modify the code below to match the Expected Output at the bottom

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

pprint(sponsor_levels)

pycon_sponsors = []

# print(pycon_sponsors_filepath)

with open(pycon_sponsors_filepath, 'r') as f:
    rows = csv.reader(f)

    header = next(f)

    for row_number, row in enumerate(rows):
        print("Row Number:\t", row_number, "Values:\t", row)

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
 
Row Number:	 0 Values:	 ['GOOG', 'ALPHABET INC.', 'VISIONARY']
Row Number:	 1 Values:	 ['AMZN', 'AMAZON COM INC', 'SUSTAINABILITY']
Row Number:	 2 Values:	 ['#N/A', 'BLOOMBERG', 'VISIONARY']
Row Number:	 3 Values:	 ['COF', 'CAPITAL ONE FINANCIAL CORP', 'MAINTAINING']
Row Number:	 4 Values:	 ['GLW', 'CORNING INC', 'MAINTAINING']
Row Number:	 5 Values:	 ['ESTC', 'ELASTIC N.V.', 'PARTNER']
Row Number:	 6 Values:	 ['FB', 'FACEBOOK INC', 'SUSTAINABILITY']
Row Number:	 7 Values:	 ['#N/A', 'HUAWEI TECHNOLOGIES', 'SUSTAINABILITY']
Row Number:	 8 Values:	 ['IBM', 'INTERNATIONAL BUSINESS MACHINES CORP', 'CONTRIBUTING']
Row Number:	 9 Values:	 ['JPM', 'JPMORGAN CHASE & CO', 'SUPPORTING']
Row Number:	 10 Values:	 ['MSFT', 'MICROSOFT CORP', 'VISIONARY']
Row Number:	 11 Values:	 ['NFLX', 'NETFLIX INC', 'PARTNER']
Row Number:	 12 Values:	 ['CRM', 'SALESFORCE.COM INC.', 'SUSTAINABILITY']
Row Number:	 13 Values:	 ['WORK', 'SLACK TECHNOLOGIES INC.', 'MAINTAINING']

Expected Output: 

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
