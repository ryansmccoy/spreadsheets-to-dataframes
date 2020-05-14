
import pandas as pd

pd.set_option('display.float_format', lambda x: f'{x:.5f}')
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)
pd.set_option('display.width', 600)

filename = r'00-data\WMT_US.csv'

df = pd.read_csv(filename)

print(df.dtypes)

"""
Ticker            object
Company Name      object
Year End          object
Total Sales        int64
Total Expenses     int64
dtype: object
"""

df['Year End'] = pd.to_datetime(df['Year End'])

print(df.dtypes)

"""
Ticker            object
Company Name      object
Year End          object
Total Sales        int64
Total Expenses     int64
dtype: object
"""

df['Total Profit'] = df['Total Sales'] - df['Total Expenses']

df['Profit Margin'] = (df['Total Profit'] / df['Total Sales']) * 100

# percent change needs to be ascending dates
df.sort_values("Year End", inplace=True)

df['Sales Growth YoY %'] = df['Total Sales'].pct_change() * 100

new_filename = filename.replace(".csv", "_pandas.csv")

df.to_csv(new_filename)
