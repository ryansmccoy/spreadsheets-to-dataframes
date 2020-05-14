
import csv
from datetime import datetime

filename = r'data\WMT_US.csv'

with open(filename, 'r') as f:
    rows = csv.reader(f)
    header = next(f)

    for row in rows:
        row_date_year = datetime.strptime(row[2], "%m/%d/%Y").year

        row_sales = int(row[3])
        row_expenses = int(row[4])

        profit = row_sales - row_expenses

        print(f"{row_date_year} Profit = {profit:,}")

"""
Output:

    2014 Profit = 16,021,999,616
    2013 Profit = 16,999,000,064
    2012 Profit = 15,699,000,320
    2011 Profit = 16,389,000,192
    2010 Profit = 14,334,999,552
    2009 Profit = 13,400,000,512
    2008 Profit = 12,730,999,808
    2007 Profit = 11,283,999,744
    2006 Profit = 11,230,999,552
    2005 Profit = 10,266,999,808
    2004 Profit = 9,054,000,128
    2003 Profit = 7,954,999,808
"""

