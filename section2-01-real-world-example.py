# Section 2 - real-world example
# requests - get data from internet
# pandas - transform & analyze data
# matplotlib - plot data
# flask - display data in browser

# https://www.sec.gov/dera/data/financial-statement-data-sets.html

# create variable of zip file url
zip_file_url = 'https://www.sec.gov/files/dera/data/financial-statement-data-sets/2021q1.zip'

# Downloading Data from Internet with Requests
# pip install requests
# https://python.readthedocs.io/en/stable/library/stdtypes.html
# https://realpython.com/python-requests/

import requests

# help(requests)

"""
import requests
r = requests.get('https://www.python.org')
r.status_code
pprint(r.content)
"""

print(f"Downloading: \t{zip_file_url}")

r = requests.get(zip_file_url)

print(f"Download Complete")

# alright, well now we need to save the file somewhere...
# there are a couple options available in the standard library
# https://docs.python.org/3.9/library/os.path.html

import os

# documentation: https://docs.python.org/3/library/os.html
# examples: https://pymotw.com/3/file_access.html
# get the current working directory or folder where python file is located

current_directory = os.getcwd()
print(current_directory)

# we can get the filename (basename) of the url using basename
basename = os.path.basename(zip_file_url)
print(basename)

zip_directory = os.path.join(current_directory, "zip-data")
print(zip_directory)

# create directory for zip files
if os.path.exists(zip_directory):
    print("Folder already Exists!")
else:
    print("Folder doesn't exist")
    os.mkdir(zip_directory)
    print("Created Directory!")

zip_file_local_filepath = os.path.join(zip_directory, basename)
print(zip_file_local_filepath)

print(f"Saving file: \t{zip_file_local_filepath}")

# context managers - https://book.pythontips.com/en/latest/context_managers.html
# binary files - https://docs.python.org/3/library/stdtypes.html#binaryseq
with open(zip_file_local_filepath, 'wb') as fd:
    fd.write(r.content)

print("Save Complete")

###### Zipfile - Read Zip files
# documentation: https://docs.python.org/3/library/zipfile.html
# examples: https://pymotw.com/3/zipfile/index.html
import zipfile

z = zipfile.ZipFile(zip_file_local_filepath)

# removing .zip from filename so can extract contents into seperate directory
zip_file_local_extract_path = zip_file_local_filepath.replace(".zip", "")

z.extractall(zip_file_local_extract_path)

###### Glob - Get list of files in Folders
# documentation: https://docs.python.org/3/library/glob.html
# examples: https://pymotw.com/3/glob/
import glob

files = glob.glob(zip_file_local_extract_path + "\\*.*")
print(files)

"""
['C:\\projects\\spreadsheets-to-dataframes\\zip-data\\2021q1\\num.txt',
 'C:\\projects\\spreadsheets-to-dataframes\\zip-data\\2021q1\\pre.txt',
 'C:\\projects\\spreadsheets-to-dataframes\\zip-data\\2021q1\\readme.htm',
 'C:\\projects\\spreadsheets-to-dataframes\\zip-data\\2021q1\\sub.txt',
 'C:\\projects\\spreadsheets-to-dataframes\\zip-data\\2021q1\\tag.txt']
"""

numbers_filepath = os.path.join(zip_file_local_extract_path, "num.txt")
print(numbers_filepath)

submissions_filepath = os.path.join(zip_file_local_extract_path, "sub.txt")
print(submissions_filepath)

########## Pandas & Resources
# https://github.com/tommyod/awesome-pandas

import pandas as pd

# fixes display of dataframes in Python Console
pd.set_option('display.float_format', lambda x: f'{x:.5f}')
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 600)

# remember from section 1 the list of dictionaries
pycon_sponsors = [{'symbol': 'GOOG', 'name': 'ALPHABET INC.', 'sponsor_level': 'VISIONARY'},
                  {'symbol': 'AMZN', 'name': 'AMAZON COM INC', 'sponsor_level': 'SUSTAINABILITY'},
                  {'symbol': '#N/A', 'name': 'BLOOMBERG', 'sponsor_level': 'VISIONARY'},
                  {'symbol': 'COF', 'name': 'CAPITAL ONE FINANCIAL CORP', 'sponsor_level': 'MAINTAINING'},
                  {'symbol': 'GLW', 'name': 'CORNING INC', 'sponsor_level': 'MAINTAINING'},
                  {'symbol': 'ESTC', 'name': 'ELASTIC N.V.', 'sponsor_level': 'PARTNER'},
                  {'symbol': 'FB', 'name': 'FACEBOOK INC', 'sponsor_level': 'SUSTAINABILITY'},
                  {'symbol': '#N/A', 'name': 'HUAWEI TECHNOLOGIES', 'sponsor_level': 'SUSTAINABILITY'},
                  {'symbol': 'IBM', 'name': 'INTERNATIONAL BUSINESS MACHINES CORP', 'sponsor_level': 'CONTRIBUTING'},
                  {'symbol': 'JPM', 'name': 'JPMORGAN CHASE & CO', 'sponsor_level': 'SUPPORTING'},
                  {'symbol': 'MSFT', 'name': 'MICROSOFT CORP', 'sponsor_level': 'VISIONARY'},
                  {'symbol': 'NFLX', 'name': 'NETFLIX INC', 'sponsor_level': 'PARTNER'},
                  {'symbol': 'CRM', 'name': 'SALESFORCE.COM INC.', 'sponsor_level': 'SUSTAINABILITY'},
                  {'symbol': 'WORK', 'name': 'SLACK TECHNOLOGIES INC.', 'sponsor_level': 'MAINTAINING'}]

# pandas loves lists of dictionaries
df_companies = pd.DataFrame(pycon_sponsors)
df_companies.head(15)

"""
Out[39]: 
   symbol                                  name   sponsor_level
0    GOOG                         ALPHABET INC.       VISIONARY
1    AMZN                        AMAZON COM INC  SUSTAINABILITY
2    #N/A                             BLOOMBERG       VISIONARY
3     COF            CAPITAL ONE FINANCIAL CORP     MAINTAINING
4     GLW                           CORNING INC     MAINTAINING
5    ESTC                          ELASTIC N.V.         PARTNER
6      FB                          FACEBOOK INC  SUSTAINABILITY
7    #N/A                   HUAWEI TECHNOLOGIES  SUSTAINABILITY
8     IBM  INTERNATIONAL BUSINESS MACHINES CORP    CONTRIBUTING
9     JPM                   JPMORGAN CHASE & CO      SUPPORTING
10   MSFT                        MICROSOFT CORP       VISIONARY
11   NFLX                           NETFLIX INC         PARTNER
12    CRM                   SALESFORCE.COM INC.  SUSTAINABILITY
13   WORK               SLACK TECHNOLOGIES INC.     MAINTAINING
"""

# export dataframe to csv
# df_companies.to_csv(r'data/pycon_sponsors.csv', index=False)

print(numbers_filepath)

df_numbers = pd.read_csv(numbers_filepath, delimiter="\t")

df_numbers.head(5)
"""
                   adsh                                          tag       version coreg     ddate  qtrs  uom          value footnote
0  0001477932-21-001167  AccountsPayableAndAccruedLiabilitiesCurrent  us-gaap/2019   NaN  20200630     0  USD    38052.00000      NaN
1  0001558370-21-002254  AccountsPayableAndAccruedLiabilitiesCurrent  us-gaap/2019   NaN  20191231     0  USD  6721000.00000      NaN
2  0001558370-21-002254  AccountsPayableAndAccruedLiabilitiesCurrent  us-gaap/2019   NaN  20201231     0  USD 11014000.00000      NaN
3  0001477932-21-001185  AccountsPayableAndAccruedLiabilitiesCurrent  us-gaap/2019   NaN  20201231     0  USD  1110598.00000      NaN
4  0001477932-21-001185  AccountsPayableAndAccruedLiabilitiesCurrent  us-gaap/2019   NaN  20191231     0  USD   751675.00000      NaN
"""
df_numbers.info()
"""
RangeIndex: 3070341 entries, 0 to 3070340
Data columns (total 9 columns):
 #   Column    Dtype
---  ------    -----
 0   adsh      object
 1   tag       object
 2   version   object
 3   coreg     object
 4   ddate     int64
 5   qtrs      int64
 6   uom       object
 7   value     float64
 8   footnote  object
dtypes: float64(1), int64(2), object(6)
memory usage: 210.8+ MB
"""
df_submissions = pd.read_csv(submissions_filepath, delimiter="\t")

df_submissions.head(5)

"""
36 columns
"""

# show dataframe sideways
# df_submissions.head(1).transpose()
df_submissions.head(1).transpose()
"""
                                           0
adsh                    0001104659-21-001067
cik                                  1452477
name                      RMR MORTGAGE TRUST
sic                                      NaN
countryba                                 US
stprba                                    MA
cityba                                NEWTON
zipba                                  02458
bas1                        TWO NEWTON PLACE
bas2        255 WASHINGTON STREET, SUITE 300
baph                            617-332-9530
countryma                                 US
stprma                                    MA
cityma                                NEWTON
zipma                                  02458
mas1                        TWO NEWTON PLACE
mas2        255 WASHINGTON STREET, SUITE 300
countryinc                                US
stprinc                                   MD
ein                                  0.00000
former           RMR REAL ESTATE INCOME FUND
changed                       20120123.00000
afs                                      NaN
wksi                                       0
fye                               1231.00000
form                                     8-K
period                        20201231.00000
fy                                       NaN
fp                                       NaN
filed                               20210106
accepted               2021-01-05 17:59:00.0
prevrpt                                    0
detail                                     0
instance               tm211580d1_8k_htm.xml
nciks                                      1
aciks                                    NaN
"""
df_submissions.info()
"""
RangeIndex: 17292 entries, 0 to 17291
Data columns (total 36 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   adsh        17292 non-null  object
 1   cik         17292 non-null  int64
 2   name        17292 non-null  object
 3   sic         17286 non-null  float64
 4   countryba   17274 non-null  object
 5   stprba      16183 non-null  object
 6   cityba      17273 non-null  object
 7   zipba       17270 non-null  object
 8   bas1        17274 non-null  object
 9   bas2        7167 non-null   object
 10  baph        17265 non-null  object
 11  countryma   17198 non-null  object
 12  stprma      16166 non-null  object
 13  cityma      17198 non-null  object
 14  zipma       17188 non-null  object
 15  mas1        17196 non-null  object
 16  mas2        7093 non-null   object
 17  countryinc  15761 non-null  object
 18  stprinc     14811 non-null  object
 19  ein         17291 non-null  float64
 20  former      9970 non-null   object
 21  changed     9970 non-null   float64
 22  afs         17129 non-null  object
 23  wksi        17292 non-null  int64
 24  fye         17228 non-null  float64
 25  form        17292 non-null  object
 26  period      17290 non-null  float64
 27  fy          6127 non-null   float64
 28  fp          6126 non-null   object
 29  filed       17292 non-null  int64
 30  accepted    17292 non-null  object
 31  prevrpt     17292 non-null  int64
 32  detail      17292 non-null  int64
 33  instance    17292 non-null  object
 34  nciks       17292 non-null  int64
 35  aciks       410 non-null    object
dtypes: float64(6), int64(6), object(24)
memory usage: 4.7+ MB
"""

# convert sic to string
df_submissions['sic'] = df_submissions['sic'].astype('Int64').astype('str')

# too many columns, many we don't really need
# to show only columns we are interested in
# can use slicing with double square brackets (just like we did with strings)
df_submissions = df_submissions[['adsh', 'cik', 'name', 'sic', 'countryba', 'stprba', 'fye', 'form', 'period', 'filed', 'instance']]
df_submissions.head(5)
"""
                       adsh      cik                            name        sic countryba stprba        fye   form         period     filed                   instance
0      0001104659-21-001067  1452477              RMR MORTGAGE TRUST        NaN        US     MA 1231.00000    8-K 20201231.00000  20210106      tm211580d1_8k_htm.xml
1      0001104659-21-001188  1804176      LONGVIEW ACQUISITION CORP. 3844.00000        US     NY 1231.00000  S-4/A 20200930.00000  20210106          lgvw-20200930.xml
2      0001104659-21-001485  1267565   COLLEGIUM PHARMACEUTICAL, INC 2834.00000        US     MA 1231.00000    8-K 20201231.00000  20210106      tm211743d1_8k_htm.xml
3      0001104659-21-001514   913277                     CLARUS CORP 3949.00000        US     UT 1231.00000    8-K 20201231.00000  20210106      tm211564d1_8k_htm.xml

"""

# Pandas Series/DataFrame - String Methods
# https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#method-summary

# filter rows in columns containing specific words
# df_submissions[df_submissions['name'].str.contains("Facebook",  flags=re.IGNORECASE, regex=True)]
# df_submissions[df_submissions['name'].str.contains("Microsoft",  flags=re.IGNORECASE, regex=True)]
# df_submissions[df_submissions['name'].str.contains("Amazon",  flags=re.IGNORECASE, regex=True)]

# standard industrial classification
sic_url = r'https://www.sec.gov/info/edgar/siccodes.htm'
# we can extract table from html by passing in url
sics_tables = pd.read_html(sic_url)
type(sics_tables)
df_sic_list = sics_tables[0]
df_sic_list.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 444 entries, 0 to 443
Data columns (total 3 columns):
 #   Column          Non-Null Count  Dtype 
---  ------          --------------  ----- 
 0   SIC Code        444 non-null    int64 
 1   Office          444 non-null    object
 2   Industry Title  444 non-null    object
dtypes: int64(1), object(2)
memory usage: 10.5+ KB
"""
# rename columns to lower, no spaces, and rename sic_code to sic
df_sic_list.columns = df_sic_list.columns.str.lower().str.replace(" ","_").str.replace("sic_code", "sic")

# convert sic column to string
df_sic_list['sic'] = df_sic_list['sic'].astype('Int64').astype('str')

# symbol to cik mapping
# we can actually read csv files from the internet directly
url = 'https://www.sec.gov/include/ticker.txt'
df_symbol_cik = pd.read_csv(url, delimiter="\t", names=['symbol', 'cik'])
df_symbol_cik.head(5)

"""
  symbol      cik
0   aapl   320193
1   msft   789019
2   amzn  1018724
3   goog  1652044
4     fb  1326801
"""

# convert column text to all upper/lower/title
# df_symbol_cik['symbol'].str.lower()
# df_symbol_cik['symbol'].str.title()
df_symbol_cik['symbol'] = df_symbol_cik['symbol'].str.upper()
df_symbol_cik.head(5)
"""
Out[57]: 
  symbol      cik
0   AAPL   320193
1   MSFT   789019
2   AMZN  1018724
3   GOOG  1652044
4     FB  1326801
"""

# create list of dataframe column names
submissions_columns = df_submissions.columns.tolist()

# VLOOKUP WITH PANDAS
# going to merge two dataframes into one
df_submissions_symbols = pd.merge(df_submissions, df_symbol_cik)

# merge sic codes onto submission dataframe
df_submissions_symbols = pd.merge(df_submissions_symbols, df_sic_list, on="sic")

# we can drop columns by name using drop
df_submissions_symbols = df_submissions_symbols.drop(columns=['instance'])

"""
Out[38]: 
                       adsh      cik                                          name   sic countryba stprba        fye   form         period     filed                        office
0      0001104659-21-001188  1804176                    LONGVIEW ACQUISITION CORP.  3844        US     NY 1231.00000  S-4/A 20200930.00000  20210106       Office of Life Sciences
1      0001157523-21-000025   859737                                   HOLOGIC INC  3844        US     MA  930.00000    8-K 20201231.00000  20210108       Office of Life Sciences
2      0001104659-21-004866  1804176                    LONGVIEW ACQUISITION CORP.  3844        US     NY 1231.00000  S-4/A 20200930.00000  20210119       Office of Life Sciences
3      0001104659-21-007341  1804176                    LONGVIEW ACQUISITION CORP.  3844        US     NY 1231.00000  S-4/A 20200930.00000  20210126       Office of Life Sciences
4      0001157523-21-000089   859737                                   HOLOGIC INC  3844        US     MA  930.00000    8-K 20210131.00000  20210127       Office of Life Sciences
                     ...      ...                                           ...   ...       ...    ...        ...    ...            ...       ...                           ...
17281  0001587650-21-000010  1587650  APPALACHIAN CONSUMER RATE RELIEF FUNDING LLC  6189        US     OH 1231.00000   10-K 20201231.00000  20210326  Office of Structured Finance
17282  0001775098-21-000005  1775098             AEP TEXAS RESTORATION FUNDING LLC  6189        US     TX 1231.00000   10-K 20201231.00000  20210326  Office of Structured Finance
17283  0001669374-21-000016  1669374      DUKE ENERGY FLORIDA PROJECT FINANCE, LLC  6189        US     FL 1231.00000   10-K 20201231.00000  20210330  Office of Structured Finance
17284  0001387131-21-004036  1449792                 PIONEER POWER SOLUTIONS, INC.  3612        US     NJ 1231.00000   10-K 20201231.00000  20210330       Office of Manufacturing
17285  0001654954-21-003567   101538                   UNITED STATES ANTIMONY CORP  3330        US     MT 1231.00000   10-K 20201231.00000  20210331       Office of Manufacturing
"""

# we can reorder columns (using pandas reindex)
# create a new list with symbol at front
new_submissions_columns = ["symbol", "industry_title"] + submissions_columns

df_submissions_symbols = df_submissions_symbols.reindex(columns=new_submissions_columns)

df_submissions_symbols.head(5)
"""
    symbol                   office                  adsh      cik                        name   sic countryba stprba        fye   form         period     filed  instance
0     BFLY  Office of Life Sciences  0001104659-21-001188  1804176  LONGVIEW ACQUISITION CORP.  3844        US     NY 1231.00000  S-4/A 20200930.00000  20210106       NaN
1  BFLY-WT  Office of Life Sciences  0001104659-21-001188  1804176  LONGVIEW ACQUISITION CORP.  3844        US     NY 1231.00000  S-4/A 20200930.00000  20210106       NaN
2     BFLY  Office of Life Sciences  0001104659-21-004866  1804176  LONGVIEW ACQUISITION CORP.  3844        US     NY 1231.00000  S-4/A 20200930.00000  20210119       NaN
3  BFLY-WT  Office of Life Sciences  0001104659-21-004866  1804176  LONGVIEW ACQUISITION CORP.  3844        US     NY 1231.00000  S-4/A 20200930.00000  20210119       NaN
4     BFLY  Office of Life Sciences  0001104659-21-007341  1804176  LONGVIEW ACQUISITION CORP.  3844        US     NY 1231.00000  S-4/A 20200930.00000  20210126       NaN
"""

ticker_list_pycon_sponsors = df_companies['symbol'].tolist()
print(ticker_list_pycon_sponsors)

# Indexing & Selecting Data
# Documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html

# Boolean Indexing: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#boolean-indexing
# Example: https://appdividend.com/2019/01/25/pandas-boolean-indexing-example-python-tutorial/
df_submissions_symbols['symbol'].isin(ticker_list_pycon_sponsors)
"""
Out[73]: 
0        False
1        False
2        False
3        False
4        False
         ...  
22129    False
22130    False
22131    False
22132    False
22133    False
Name: symbol, Length: 22134, dtype: bool
"""

df_pycon_symbols = df_submissions_symbols[df_submissions_symbols['symbol'].isin(ticker_list_pycon_sponsors)]

df_pycon_symbols.drop_duplicates("symbol").sort_values('symbol')

"""
Out[77]: 
      symbol                  adsh      cik                                  name        sic countryba stprba        fye  form         period     filed                 instance
10626   AMZN  0001193125-21-018066  1018724                        AMAZON COM INC 5961.00000        US     WA 1231.00000   8-K 20210131.00000  20210127        d30366d8k_htm.xml
11800    COF  0000927628-21-000015   927628            CAPITAL ONE FINANCIAL CORP 6021.00000        US     VA 1231.00000   8-K 20210131.00000  20210126     cof-20210126_htm.xml
17182    CRM  0001193125-21-045220  1108524                  SALESFORCE.COM, INC. 7372.00000        US     CA  131.00000   8-K 20210228.00000  20210216       d125434d8k_htm.xml
8686    ESTC  0001707753-21-000004  1707753                          ELASTIC N.V. 7372.00000        NL    NaN  430.00000   8-K 20201231.00000  20210114    estc-20210114_htm.xml
11596     FB  0001326801-21-000014  1326801                          FACEBOOK INC 7370.00000        US     CA 1231.00000  10-K 20201231.00000  20210128      fb-20201231_htm.xml
12364    GLW  0000024741-21-000007    24741                       CORNING INC /NY 3357.00000        US     NY 1231.00000   8-K 20210131.00000  20210127  glw-20210127x8k_htm.xml
13697   GOOG  0001652044-21-000010  1652044                         ALPHABET INC. 7370.00000        US     CA 1231.00000  10-K 20201231.00000  20210203    goog-20201231_htm.xml
8502     IBM  0001558370-21-000327    51143  INTERNATIONAL BUSINESS MACHINES CORP 3570.00000        US     NY 1231.00000   8-K 20210131.00000  20210121  ibm-20210121x8k_htm.xml
7850     JPM  0000019617-21-000123    19617                   JPMORGAN CHASE & CO 6021.00000        US     NY 1231.00000   8-K 20210131.00000  20210121     jpm-20210121_htm.xml
12145   MSFT  0001193125-21-017683   789019                        MICROSOFT CORP 7372.00000        US     WA  630.00000   8-K 20210131.00000  20210126        d65802d8k_htm.xml
9415    NFLX  0001065280-21-000037  1065280                           NETFLIX INC 7841.00000        US     CA 1231.00000   8-K 20210131.00000  20210119    nflx-20210119_htm.xml
15646   WORK  0001193125-21-037224  1764925              SLACK TECHNOLOGIES, INC. 7372.00000        US     CA  131.00000   8-K 20210131.00000  20210211        d11789d8k_htm.xml
"""

# let's reorder columns
# create list of column names
submissions_symbols_columns = df_pycon_symbols.columns.tolist()

new_submissions_columns = ['cik',
                           'symbol',
                           'name',
                           'sic',
                           'industry_title',
                           'countryba',
                           'stprba',
                           'fye',
                           'form',
                           'period',
                           'filed',
                           'adsh'
                           ]

df_pycon_symbols = df_pycon_symbols.reindex(columns=new_submissions_columns)
df_pycon_symbols.drop_duplicates("symbol").sort_values('symbol')

"""
Out[73]: 
           cik symbol                                  name   sic                                     industry_title countryba stprba        fye  form         period     filed                  adsh
7720   1018724   AMZN                        AMAZON COM INC  5961                 RETAIL-CATALOG & MAIL-ORDER HOUSES        US     WA 1231.00000   8-K 20210131.00000  20210127  0001193125-21-018066
10276   927628    COF            CAPITAL ONE FINANCIAL CORP  6021                          NATIONAL COMMERCIAL BANKS        US     VA 1231.00000   8-K 20210131.00000  20210126  0000927628-21-000015
12824  1108524    CRM                  SALESFORCE.COM, INC.  7372                      SERVICES-PREPACKAGED SOFTWARE        US     CA  131.00000   8-K 20210228.00000  20210216  0001193125-21-045220
12603  1707753   ESTC                          ELASTIC N.V.  7372                      SERVICES-PREPACKAGED SOFTWARE        NL    NaN  430.00000   8-K 20201231.00000  20210114  0001707753-21-000004
17111  1326801     FB                          FACEBOOK INC  7370  SERVICES-COMPUTER PROGRAMMING, DATA PROCESSING...        US     CA 1231.00000  10-K 20201231.00000  20210128  0001326801-21-000014
20978    24741    GLW                       CORNING INC /NY  3357            DRAWING & INSULATING OF NONFERROUS WIRE        US     NY 1231.00000   8-K 20210131.00000  20210127  0000024741-21-000007
17120  1652044   GOOG                         ALPHABET INC.  7370  SERVICES-COMPUTER PROGRAMMING, DATA PROCESSING...        US     CA 1231.00000  10-K 20201231.00000  20210203  0001652044-21-000010
20783    51143    IBM  INTERNATIONAL BUSINESS MACHINES CORP  3570                        COMPUTER & OFFICE EQUIPMENT        US     NY 1231.00000   8-K 20210131.00000  20210121  0001558370-21-000327
9787     19617    JPM                   JPMORGAN CHASE & CO  6021                          NATIONAL COMMERCIAL BANKS        US     NY 1231.00000   8-K 20210131.00000  20210121  0000019617-21-000123
12676   789019   MSFT                        MICROSOFT CORP  7372                      SERVICES-PREPACKAGED SOFTWARE        US     WA  630.00000   8-K 20210131.00000  20210126  0001193125-21-017683
21008  1065280   NFLX                           NETFLIX INC  7841                         SERVICES-VIDEO TAPE RENTAL        US     CA 1231.00000   8-K 20210131.00000  20210119  0001065280-21-000037
12767  1764925   WORK              SLACK TECHNOLOGIES, INC.  7372                      SERVICES-PREPACKAGED SOFTWARE        US     CA  131.00000   8-K 20210131.00000  20210211  0001193125-21-037224

"""

df_pycon_symbols['symbol'].unique()

"""
array(['JPM', 'IBM', 'ESTC', 'NFLX', 'AMZN', 'FB', 'COF', 'MSFT', 'GLW',
       'GOOG', 'WORK', 'CRM'], dtype=object)
"""

df_pycon_symbols['symbol'].nunique()

"""
12
"""

# https://kanoki.org/2019/11/12/how-to-use-regex-in-pandas/
# https://www.dataquest.io/blog/regular-expressions-data-scientists/
import re  # regular expression

# Interested in Revenues for Annual (Full-Year) & Quarter (3-months)
# Form 10-K & 10-Q
# Filtering Values in a column
df_pycon_symbols[df_pycon_symbols['form'] == '10-K']
"""
Out[82]: 
           cik symbol                                  name        sic countryba stprba        fye  form         period     filed                  instance                  adsh
7895     19617    JPM                   JPMORGAN CHASE & CO 6021.00000        US     NY 1231.00000  10-K 20201231.00000  20210223      jpm-20201231_htm.xml  0000019617-21-000236
8505     51143    IBM  INTERNATIONAL BUSINESS MACHINES CORP 3570.00000        US     NY 1231.00000  10-K 20201231.00000  20210223  ibm-20201231x10k_htm.xml  0001558370-21-001489
9416   1065280   NFLX                           NETFLIX INC 7841.00000        US     CA 1231.00000  10-K 20201231.00000  20210128     nflx-20201231_htm.xml  0001065280-21-000040
10627  1018724   AMZN                        AMAZON COM INC 5961.00000        US     WA 1231.00000  10-K 20201231.00000  20210203     amzn-20201231_htm.xml  0001018724-21-000004
11596  1326801     FB                          FACEBOOK INC 7370.00000        US     CA 1231.00000  10-K 20201231.00000  20210128       fb-20201231_htm.xml  0001326801-21-000014
11856   927628    COF            CAPITAL ONE FINANCIAL CORP 6021.00000        US     VA 1231.00000  10-K 20201231.00000  20210225      cof-20201231_htm.xml  0000927628-21-000094
12367    24741    GLW                       CORNING INC /NY 3357.00000        US     NY 1231.00000  10-K 20201231.00000  20210212  glw-20201231x10k_htm.xml  0001562762-21-000023
13697  1652044   GOOG                         ALPHABET INC. 7370.00000        US     CA 1231.00000  10-K 20201231.00000  20210203     goog-20201231_htm.xml  0001652044-21-000010
15653  1764925   WORK              SLACK TECHNOLOGIES, INC. 7372.00000        US     CA  131.00000  10-K 20210131.00000  20210319     work-20210131_htm.xml  0001764925-21-000050
17185  1108524    CRM                  SALESFORCE.COM, INC. 7372.00000        US     CA  131.00000  10-K 20210131.00000  20210317      crm-20210131_htm.xml  0001108524-21-000014
"""

# filter on multiple values
# | (pipe or vertical bar) means or
df_pycon_symbols.loc[(df_pycon_symbols['form'] == '10-K') | (df_pycon_symbols['form'] == '10-Q')]
# using .isin() method
df_pycon_symbols[df_pycon_symbols['form'].isin(['10-K', '10-Q'])]
"""
Out[83]: 
           cik symbol                                  name        sic countryba stprba        fye  form         period     filed                   instance                  adsh
7895     19617    JPM                   JPMORGAN CHASE & CO 6021.00000        US     NY 1231.00000  10-K 20201231.00000  20210223       jpm-20201231_htm.xml  0000019617-21-000236
8505     51143    IBM  INTERNATIONAL BUSINESS MACHINES CORP 3570.00000        US     NY 1231.00000  10-K 20201231.00000  20210223   ibm-20201231x10k_htm.xml  0001558370-21-001489
8688   1707753   ESTC                          ELASTIC N.V. 7372.00000        NL    NaN  430.00000  10-Q 20210131.00000  20210303      estc-20210131_htm.xml  0001707753-21-000012
9416   1065280   NFLX                           NETFLIX INC 7841.00000        US     CA 1231.00000  10-K 20201231.00000  20210128      nflx-20201231_htm.xml  0001065280-21-000040
10627  1018724   AMZN                        AMAZON COM INC 5961.00000        US     WA 1231.00000  10-K 20201231.00000  20210203      amzn-20201231_htm.xml  0001018724-21-000004
11596  1326801     FB                          FACEBOOK INC 7370.00000        US     CA 1231.00000  10-K 20201231.00000  20210128        fb-20201231_htm.xml  0001326801-21-000014
11856   927628    COF            CAPITAL ONE FINANCIAL CORP 6021.00000        US     VA 1231.00000  10-K 20201231.00000  20210225       cof-20201231_htm.xml  0000927628-21-000094
12146   789019   MSFT                        MICROSOFT CORP 7372.00000        US     WA  630.00000  10-Q 20201231.00000  20210126  msft-10q_20201231_htm.xml  0001564590-21-002316
12367    24741    GLW                       CORNING INC /NY 3357.00000        US     NY 1231.00000  10-K 20201231.00000  20210212   glw-20201231x10k_htm.xml  0001562762-21-000023
13697  1652044   GOOG                         ALPHABET INC. 7370.00000        US     CA 1231.00000  10-K 20201231.00000  20210203      goog-20201231_htm.xml  0001652044-21-000010
15653  1764925   WORK              SLACK TECHNOLOGIES, INC. 7372.00000        US     CA  131.00000  10-K 20210131.00000  20210319      work-20210131_htm.xml  0001764925-21-000050
17185  1108524    CRM                  SALESFORCE.COM, INC. 7372.00000        US     CA  131.00000  10-K 20210131.00000  20210317       crm-20210131_htm.xml  0001108524-21-000014

"""
# using str method which has a contains method
df_pycon_symbols[df_pycon_symbols['form'].str.contains('(10-K|10-Q)', regex=True)]
"""
Out[84]: 
           cik symbol                                  name        sic countryba stprba        fye  form         period     filed                   instance                  adsh
7895     19617    JPM                   JPMORGAN CHASE & CO 6021.00000        US     NY 1231.00000  10-K 20201231.00000  20210223       jpm-20201231_htm.xml  0000019617-21-000236
8505     51143    IBM  INTERNATIONAL BUSINESS MACHINES CORP 3570.00000        US     NY 1231.00000  10-K 20201231.00000  20210223   ibm-20201231x10k_htm.xml  0001558370-21-001489
8688   1707753   ESTC                          ELASTIC N.V. 7372.00000        NL    NaN  430.00000  10-Q 20210131.00000  20210303      estc-20210131_htm.xml  0001707753-21-000012
9416   1065280   NFLX                           NETFLIX INC 7841.00000        US     CA 1231.00000  10-K 20201231.00000  20210128      nflx-20201231_htm.xml  0001065280-21-000040
10627  1018724   AMZN                        AMAZON COM INC 5961.00000        US     WA 1231.00000  10-K 20201231.00000  20210203      amzn-20201231_htm.xml  0001018724-21-000004
11596  1326801     FB                          FACEBOOK INC 7370.00000        US     CA 1231.00000  10-K 20201231.00000  20210128        fb-20201231_htm.xml  0001326801-21-000014
11856   927628    COF            CAPITAL ONE FINANCIAL CORP 6021.00000        US     VA 1231.00000  10-K 20201231.00000  20210225       cof-20201231_htm.xml  0000927628-21-000094
12146   789019   MSFT                        MICROSOFT CORP 7372.00000        US     WA  630.00000  10-Q 20201231.00000  20210126  msft-10q_20201231_htm.xml  0001564590-21-002316
12367    24741    GLW                       CORNING INC /NY 3357.00000        US     NY 1231.00000  10-K 20201231.00000  20210212   glw-20201231x10k_htm.xml  0001562762-21-000023
13697  1652044   GOOG                         ALPHABET INC. 7370.00000        US     CA 1231.00000  10-K 20201231.00000  20210203      goog-20201231_htm.xml  0001652044-21-000010
15653  1764925   WORK              SLACK TECHNOLOGIES, INC. 7372.00000        US     CA  131.00000  10-K 20210131.00000  20210319      work-20210131_htm.xml  0001764925-21-000050
17185  1108524    CRM                  SALESFORCE.COM, INC. 7372.00000        US     CA  131.00000  10-K 20210131.00000  20210317       crm-20210131_htm.xml  0001108524-21-000014
"""
# using str method which has a contains method with regex
df_pycon_symbols[df_pycon_symbols['form'].str.contains('10-', flags=re.IGNORECASE, regex=True)]
"""
Out[87]: 
           cik symbol                                  name        sic countryba stprba        fye  form         period     filed                   instance                  adsh
7895     19617    JPM                   JPMORGAN CHASE & CO 6021.00000        US     NY 1231.00000  10-K 20201231.00000  20210223       jpm-20201231_htm.xml  0000019617-21-000236
8505     51143    IBM  INTERNATIONAL BUSINESS MACHINES CORP 3570.00000        US     NY 1231.00000  10-K 20201231.00000  20210223   ibm-20201231x10k_htm.xml  0001558370-21-001489
8688   1707753   ESTC                          ELASTIC N.V. 7372.00000        NL    NaN  430.00000  10-Q 20210131.00000  20210303      estc-20210131_htm.xml  0001707753-21-000012
9416   1065280   NFLX                           NETFLIX INC 7841.00000        US     CA 1231.00000  10-K 20201231.00000  20210128      nflx-20201231_htm.xml  0001065280-21-000040
10627  1018724   AMZN                        AMAZON COM INC 5961.00000        US     WA 1231.00000  10-K 20201231.00000  20210203      amzn-20201231_htm.xml  0001018724-21-000004
11596  1326801     FB                          FACEBOOK INC 7370.00000        US     CA 1231.00000  10-K 20201231.00000  20210128        fb-20201231_htm.xml  0001326801-21-000014
11856   927628    COF            CAPITAL ONE FINANCIAL CORP 6021.00000        US     VA 1231.00000  10-K 20201231.00000  20210225       cof-20201231_htm.xml  0000927628-21-000094
12146   789019   MSFT                        MICROSOFT CORP 7372.00000        US     WA  630.00000  10-Q 20201231.00000  20210126  msft-10q_20201231_htm.xml  0001564590-21-002316
12367    24741    GLW                       CORNING INC /NY 3357.00000        US     NY 1231.00000  10-K 20201231.00000  20210212   glw-20201231x10k_htm.xml  0001562762-21-000023
13697  1652044   GOOG                         ALPHABET INC. 7370.00000        US     CA 1231.00000  10-K 20201231.00000  20210203      goog-20201231_htm.xml  0001652044-21-000010
15653  1764925   WORK              SLACK TECHNOLOGIES, INC. 7372.00000        US     CA  131.00000  10-K 20210131.00000  20210319      work-20210131_htm.xml  0001764925-21-000050
17185  1108524    CRM                  SALESFORCE.COM, INC. 7372.00000        US     CA  131.00000  10-K 20210131.00000  20210317       crm-20210131_htm.xml  0001108524-21-000014

"""

filing_ids = df_submissions['adsh'].drop_duplicates().tolist()

df_revenues = df_numbers[df_numbers['tag'].str.contains("Revenues", flags=re.IGNORECASE, regex=True)]
"""
                         adsh       tag               version coreg     ddate  qtrs  uom              value footnote
2270763  0000104169-21-000033  Revenues          us-gaap/2020   NaN  20210131     4  USD 559151000000.00000      NaN
2270765  0000104169-21-000033  Revenues          us-gaap/2020   NaN  20200131     4  USD 523964000000.00000      NaN
2270764  0000104169-21-000033  Revenues          us-gaap/2020   NaN  20190131     4  USD 514405000000.00000      NaN
2535895  0001306965-21-000025   Revenue             ifrs/2020   NaN  20181231     4  USD 388379000000.00000      NaN
2535896  0001306965-21-000025   Revenue             ifrs/2020   NaN  20191231     4  USD 344877000000.00000      NaN
"""
# let's see which tag is the most popular
df_revenues.groupby("tag").count().sort_values('adsh', ascending=False).head(10)
# help(df_revenues.groupby)

"""
Out[92]: 
                                                     adsh  version  coreg  ddate   qtrs    uom  value  footnote
tag                                                                                                            
Revenues                                            11793    11793    592  11793  11793  11793  11420        15
RevenuesNetOfInterestExpense                          257      257      2    257    257    257    257         1
TaxEffectOfRevenuesExemptFromTaxation2011             124      124      0    124    124    124    124         0
RelatedPartyTransactionOtherRevenuesFromTransac...     83       83     11     83     83     83     83         1
OtherRevenues                                          52       52      3     52     52     52     52         3
RevenuesExcludingInterestAndDividends                  41       41      0     41     41     41     37         0
TaxRateEffectOfRevenuesExemptFromTaxation              27       27      0     27     27     27     27         0
SalesRevenuesNet                                       26       26     16     26     26     26     26         0
IncreaseDecreaseInDeferredRevenues                     23       23      0     23     23     23     23         0
RevenuesAndOtherIncome                                 20       20      0     20     20     20     20         0

"""

df_revenues = df_numbers[df_numbers['tag'].isin(['Revenues'])]

df_revenues.head(5)
"""
Out[95]: 
                       adsh       tag       version coreg     ddate  qtrs  uom         value footnote
36447  0001683168-21-000527  Revenues  us-gaap/2019   NaN  20181231     4  USD  308129.00000      NaN
36448  0001683168-21-000527  Revenues  us-gaap/2019   NaN  20190930     1  USD  439288.00000      NaN
36449  0001683168-21-000527  Revenues  us-gaap/2019   NaN  20190930     3  USD 1111690.00000      NaN
36450  0001683168-21-000527  Revenues  us-gaap/2019   NaN  20191231     4  USD 1460370.00000      NaN
36451  0001683168-21-000527  Revenues  us-gaap/2019   NaN  20200930     1  USD  544003.00000      NaN
"""
df_revenues.sort_values('value')
"""
Out[96]: 
                         adsh       tag       version coreg     ddate  qtrs  uom             value footnote
2270737  0000881453-21-000010  Revenues  us-gaap/2020   NaN  20200630     1  USD -2640794000.00000      NaN
2270733  0000881453-21-000010  Revenues  us-gaap/2020   NaN  20201231     4  USD -2225424000.00000      NaN
2267729  0001104659-21-029202  Revenues  us-gaap/2020   NaN  20201231     4  USD -1876885171.00000      NaN
2267725  0001104659-21-029202  Revenues  us-gaap/2020   NaN  20200331     1  USD -1614034624.00000      NaN
2262387  0001527469-21-000025  Revenues  us-gaap/2020   NaN  20200331     1  USD -1549000000.00000      NaN
[11793 rows x 9 columns]
"""

df_revenues = df_revenues.sort_values('value', ascending=False)
df_revenues.head(5)
"""
Out[99]: 
                         adsh       tag       version coreg     ddate  qtrs  uom               value footnote
36489    0001193125-21-039771  Revenues  us-gaap/2019   NaN  20191231     3  JPY 1717785000000.00000      NaN
36491    0001193125-21-039771  Revenues  us-gaap/2019   NaN  20201231     3  JPY 1665694000000.00000      NaN
36488    0001193125-21-039771  Revenues  us-gaap/2019   NaN  20191231     1  JPY  582340000000.00000      NaN
36490    0001193125-21-039771  Revenues  us-gaap/2019   NaN  20201231     1  JPY  580956000000.00000      NaN
2270763  0000104169-21-000033  Revenues  us-gaap/2020   NaN  20210131     4  USD  559151000000.00000      NaN

"""
df_revenues['uom'].unique()
"""
Out[101]: array(['JPY', 'USD', 'CNY', 'CAD', 'CHF', 'HKD', 'EUR'], dtype=object)
"""
# filter column to show only USD or EUR
df_revenues = df_revenues[(df_revenues['uom'] == "USD") | (df_revenues['uom'] == "EUR")]

df_revenues.head(5)
"""
Out[108]: 
                         adsh       tag       version coreg     ddate  qtrs  uom              value footnote
2270763  0000104169-21-000033  Revenues  us-gaap/2020   NaN  20210131     4  USD 559151000000.00000      NaN
2270765  0000104169-21-000033  Revenues  us-gaap/2020   NaN  20200131     4  USD 523964000000.00000      NaN
2270764  0000104169-21-000033  Revenues  us-gaap/2020   NaN  20190131     4  USD 514405000000.00000      NaN
37010    0000034088-21-000012  Revenues  us-gaap/2019   NaN  20181231     4  USD 290212000000.00000      NaN
2265157  0000064803-21-000011  Revenues  us-gaap/2020   NaN  20201231     4  USD 268706000000.00000      NaN
"""
df_revenues.tail(5)
"""
Out[109]: 
                         adsh       tag       version coreg     ddate  qtrs  uom  value footnote
2271942  0001437749-21-007538  Revenues  us-gaap/2020   NaN  20191231     4  USD    NaN      NaN
2271949  0001344676-21-000014  Revenues  us-gaap/2020   NaN  20201231     4  USD    NaN      NaN
2271950  0001344676-21-000014  Revenues  us-gaap/2020   NaN  20191231     4  USD    NaN      NaN
2271973  0001213900-21-018695  Revenues  us-gaap/2020   NaN  20201231     2  USD    NaN      NaN
2271980  0001213900-21-018451  Revenues  us-gaap/2020   NaN  20201231     4  USD    NaN      NaN
"""

df_revenues = df_revenues.dropna(subset=['value'])

# filter by 10-Q\K
df_submissions_symbols = df_submissions_symbols[df_submissions_symbols['form'].str.contains('10-', flags=re.IGNORECASE, regex=True)]
# we can only show first 8 columns using the iloc
df_submissions_symbols.iloc[:,:8]
"""
           cik symbol                                  name   sic                                     industry_title countryba stprba        fye
7721   1018724   AMZN                        AMAZON COM INC  5961                 RETAIL-CATALOG & MAIL-ORDER HOUSES        US     WA 1231.00000
9832     19617    JPM                   JPMORGAN CHASE & CO  6021                          NATIONAL COMMERCIAL BANKS        US     NY 1231.00000
10332   927628    COF            CAPITAL ONE FINANCIAL CORP  6021                          NATIONAL COMMERCIAL BANKS        US     VA 1231.00000
12605  1707753   ESTC                          ELASTIC N.V.  7372                      SERVICES-PREPACKAGED SOFTWARE        NL    NaN  430.00000
12677   789019   MSFT                        MICROSOFT CORP  7372                      SERVICES-PREPACKAGED SOFTWARE        US     WA  630.00000
12774  1764925   WORK              SLACK TECHNOLOGIES, INC.  7372                      SERVICES-PREPACKAGED SOFTWARE        US     CA  131.00000
12827  1108524    CRM                  SALESFORCE.COM, INC.  7372                      SERVICES-PREPACKAGED SOFTWARE        US     CA  131.00000
17111  1326801     FB                          FACEBOOK INC  7370  SERVICES-COMPUTER PROGRAMMING, DATA PROCESSING...        US     CA 1231.00000
17120  1652044   GOOG                         ALPHABET INC.  7370  SERVICES-COMPUTER PROGRAMMING, DATA PROCESSING...        US     CA 1231.00000
20786    51143    IBM  INTERNATIONAL BUSINESS MACHINES CORP  3570                        COMPUTER & OFFICE EQUIPMENT        US     NY 1231.00000
20981    24741    GLW                       CORNING INC /NY  3357            DRAWING & INSULATING OF NONFERROUS WIRE        US     NY 1231.00000
21009  1065280   NFLX                           NETFLIX INC  7841                         SERVICES-VIDEO TAPE RENTAL        US     CA 1231.00000
"""

# left = df_numbers
# right = df_submissions
df_submission_numbers = pd.merge(df_numbers, df_submissions_symbols, left_on='adsh', right_on='adsh', how='inner')
df_submission_numbers.head(3).transpose()
"""
                                                          0                                            1                            2
adsh                                   0001558370-21-002254                         0001558370-21-002254         0001558370-21-002254
tag             AccountsPayableAndAccruedLiabilitiesCurrent  AccountsPayableAndAccruedLiabilitiesCurrent       AccountsPayableCurrent
version                                        us-gaap/2019                                 us-gaap/2019                 us-gaap/2019
coreg                                                   NaN                                          NaN                          NaN
ddate                                              20191231                                     20201231                     20191231
qtrs                                                      0                                            0                            0
uom                                                     USD                                          USD                          USD
value                                         6721000.00000                               11014000.00000                4152000.00000
footnote                                                NaN                                          NaN                          NaN
cik                                                 1034842                                      1034842                      1034842
symbol                                                 RIGL                                         RIGL                         RIGL
name                              RIGEL PHARMACEUTICALS INC                    RIGEL PHARMACEUTICALS INC    RIGEL PHARMACEUTICALS INC
sic                                                    2834                                         2834                         2834
industry_title                  PHARMACEUTICAL PREPARATIONS                  PHARMACEUTICAL PREPARATIONS  PHARMACEUTICAL PREPARATIONS
countryba                                                US                                           US                           US
stprba                                                   CA                                           CA                           CA
fye                                              1231.00000                                   1231.00000                   1231.00000
form                                                   10-K                                         10-K                         10-K
period                                       20201231.00000                               20201231.00000               20201231.00000
filed                                              20210302                                     20210302                     20210302
"""

df_submission_numbers.sort_values(['symbol', 'tag']).head(5)

df_submission_numbers.columns.tolist()

new_column_order = ['cik',
                    'symbol',
                    'name',
                    'sic',
                    'industry_title',
                    'countryba',
                    'stprba',
                    'fye',
                    'form',
                    'period',
                    'filed',
                    'adsh',
                    'tag',
                    'version',
                    'coreg',
                    'ddate',
                    'qtrs',
                    'uom',
                    'value'
                    ]

# reorder columns
df_submission_numbers = df_submission_numbers.reindex(columns=new_column_order)

# find most common tag
df_submission_numbers.groupby("tag").count().sort_values('adsh', ascending=False).head(5)

"""
Questions:
- Which company generates the most revenues/sales?
- Which company has the fastest growing revenues/sales?
- Which company has the largest stockpile of cash?
- Which company spends the most on expenses?
- which company is the most profitable?
"""

# Group by: split-apply-combine
df_revenues = df_submission_numbers[df_submission_numbers['tag'].isin(["Revenues"])]

# only show companies with 4 quarters (1 year) worth of data
df_revenues = df_revenues[df_revenues['qtrs']==4]

# largest revenues by company
df_revenues.sort_values('value', ascending=False).head(25)

df_revenues.drop_duplicates('ddate')

# want to make sure dates are sorted correctly, newest being first
df_revenues = df_revenues.sort_values('ddate', ascending=True)

# group by symbol
df_groups_symbol = df_revenues.groupby(["symbol","qtrs"])
df_group_symbol = df_groups_symbol.get_group(('WMT', 4))

"""
           cik symbol          name   sic         industry_title countryba stprba       fye  form         period     filed                  adsh       tag       version coreg     ddate  qtrs  uom              value
608365  104169    WMT  WALMART INC.  5331  RETAIL-VARIETY STORES        US     AR 131.00000  10-K 20210131.00000  20210319  0000104169-21-000033  Revenues  us-gaap/2020   NaN  20190131     4  USD 514405000000.00000
608366  104169    WMT  WALMART INC.  5331  RETAIL-VARIETY STORES        US     AR 131.00000  10-K 20210131.00000  20210319  0000104169-21-000033  Revenues  us-gaap/2020   NaN  20200131     4  USD 523964000000.00000
608364  104169    WMT  WALMART INC.  5331  RETAIL-VARIETY STORES        US     AR 131.00000  10-K 20210131.00000  20210319  0000104169-21-000033  Revenues  us-gaap/2020   NaN  20210131     4  USD 559151000000.00000
"""
df_group_symbol['value']
"""
Out[214]: 
608365   514405000000.00000
608366   523964000000.00000
608364   559151000000.00000
"""
import matplotlib.pyplot as plt
plt.close("all")

df_group_symbol['pct_change'] = df_group_symbol['value'].pct_change()

df_group_symbol.set_index('ddate')['pct_change'].plot(kind="bar")
plt.show()

"""
Out[213]: 
608365       NaN
608366   0.01858
608364   0.06716
Name: value, dtype: float64

"""

group = []

for (symbol, qtrs), df_group in df_revenues.groupby(["symbol","qtrs"]):
    df_group['pct_change'] = df_group['value'].pct_change()
    group.append(df_group)

df_revenues_pct = pd.concat(group)

df_revenues_pct = df_revenues_pct.dropna(subset=['pct_change'])
df_revenues_pct.sort_values('value', ascending=False).head(25)

"""
Out[235]: 
             cik symbol                    name   sic                                     industry_title countryba stprba        fye  form         period     filed                  adsh       tag       version coreg     ddate  qtrs  uom              value  pct_change
608364    104169    WMT            WALMART INC.  5331                              RETAIL-VARIETY STORES        US     AR  131.00000  10-K 20210131.00000  20210319  0000104169-21-000033  Revenues  us-gaap/2020   NaN  20210131     4  USD 559151000000.00000     0.06716
608366    104169    WMT            WALMART INC.  5331                              RETAIL-VARIETY STORES        US     AR  131.00000  10-K 20210131.00000  20210319  0000104169-21-000033  Revenues  us-gaap/2020   NaN  20200131     4  USD 523964000000.00000     0.01858
2619820    64803    CVS         CVS HEALTH CORP  5912          RETAIL-DRUG STORES AND PROPRIETARY STORES        US     RI 1231.00000  10-K 20201231.00000  20210216  0000064803-21-000011  Revenues  us-gaap/2020   NaN  20201231     4  USD 268706000000.00000     0.04646
8423       34088    XOM        EXXON MOBIL CORP  2911                                 PETROLEUM REFINING        US     TX 1231.00000  10-K 20201231.00000  20210224  0000034088-21-000012  Revenues  us-gaap/2019   NaN  20191231     4  USD 264938000000.00000    -0.08709
1123462   731766    UNH  UNITEDHEALTH GROUP INC  6324                   HOSPITAL & MEDICAL SERVICE PLANS        US     MN 1231.00000  10-K 20201231.00000  20210301  0000731766-21-000013  Revenues  us-gaap/2020   NaN  20201231     4  USD 257141000000.00000     0.06189'
"""

df_revenues_pct['pct_change'] > 0

"""
Out[9]: 
517035     False
2303777    False
2303782    False
2620735    False
2620734     True
           ...  
139256      True
139257      True
145650     False
1646285    False
1742589     True
Name: pct_change, Length: 3667, dtype: bool
"""

df_revenues_pct = df_revenues_pct[df_revenues_pct['pct_change'] > 0]

df_revenues_pct['ddate'].sort_values(ascending=False)
"""
Out[13]: 
2916979    20211231
2923313    20210131
610356     20210131
608364     20210131
3020974    20210131
             ...   
3283488    20181231
3283449    20181231
1889364    20181231
721424     20181231
3229689    20181231
"""

df_revenues_pct = df_revenues_pct.sort_values('ddate', ascending=False)

# delete old quarters
df_revenues_pct = df_revenues_pct.drop_duplicates(keep='first', subset=['cik']).sort_values('value', ascending=False)

df_revenues_pct.sort_values('pct_change', ascending=False).head(25)


