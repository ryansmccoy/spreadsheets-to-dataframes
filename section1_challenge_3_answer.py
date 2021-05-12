# Perform an Excel VLOOKUP with a Python Dictionary

# Challenge 3
# Create a function that takes a filepath as a parameter and returns the sum of donations

import csv
import os
from pprint import pprint

current_directory = os.getcwd()

pycon_sponsors_filename = 'pycon_sponsors.csv'
pycon_sponsors_filepath = os.path.join(current_directory, "data", pycon_sponsors_filename)

print(pycon_sponsors_filepath)

def sum_donations(filepath):

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

    pycon_sum = []

    with open(filepath, 'r') as f:
        rows = csv.reader(f)

        header = next(f)

        for row_number, row in enumerate(rows):
            ticker, name, level = row
            value = int(sponsor_vlookup[row[2]])
            pycon_sum.append(value)

    return pycon_sum


"""
Output:

pycon_sum = sum_donation(pycon_sponsors_filepath)

print("Total Donation:\t", pycon_sum)

"""
