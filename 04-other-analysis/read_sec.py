
import pandas as pd

df = pd.DataFrame()

df.from_csv(files)


subs = []

for filename in files:
    print(f"Companies in {filename}")
    zip_filepath = os.path.join(folder_path, filename)
    data_file = zipfile.ZipFile(zip_filepath)

    df_sub = pd.read_csv(data_file.open('sub.txt'), sep='\t', error_bad_lines=False)

    subs.append(df_sub)

revenues = []
for filename in files:
    print(f"Companies in {filename}")
    zip_filepath = os.path.join(folder_path, filename)
    data_file = zipfile.ZipFile(zip_filepath)

    df_num = pd.read_csv(data_file.open('num.txt'), encoding="latin1", sep='\t', error_bad_lines=False)
    df_revenues = df_num[df_num['tag'].str.contains('Revenues', regex=True)]
    revenues.append(df_revenues)

df_revs = pd.concat(revenues)

df_revs.sort_values('ddate', inplace=True)
df_revs['cik'] = df_revs['adsh'].apply(lambda x: x.split("-")[0])

for i, df_group in df_revs.groupby('cik'):
    print(df_group)

# df_sub_nodupes = df_sub.drop_duplicates(subset='name')
# df_sub_nodupes.head(100)

# df['stprinc'].drop_duplicates()

df_missouri = df_sub[(df_sub['stprinc'].isin(['MO']) | df_sub['stprma'].isin(['MO'])) ]
print(df_missouri[df_missouri['form'].isin(['10-K'])].sort_values('name'))

df_sec_symbols = pd.read_json(r'D:\PROJECTS\presentations\meetup-2019-spreadsheets-to-dataframes\company_tickers.json').T

"""
curl "https://api-global.morningstar.com/sal-service/v1/stock/newfinancials/0P0000014I/incomeStatement/detail?dataType=A^&reportType=A^&locale=en^&^&operation=export" -H "Sec-Fetch-Mode: cors" -H "Origin: https://www.morningstar.com" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36" -H "Accept: application/json, text/plain, */*" -H "Referer: https://www.morningstar.com/stocks/xnys/cat/financials" -H "X-API-RequestId: 52a823bc-0d1f-6c2a-51a9-fb553553a192" -H "ApiKey: lstzFDEOhfFNMLikKa0am9mgEKLBl49T" -H "X-API-REALTIME-E: eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.XmuAS3x5r-0MJuwLDdD4jNC6zjsY7HAFNo2VdvGg6jGcj4hZ4NaJgH20ez313H8An9UJrsUj8ERH0R8UyjQu2UGMUnJ5B1ooXFPla0LQEbN_Em3-IG84YPFcWVmEgcs1Fl2jjlKHVqZp04D21UvtgQ4xyPwQ-QDdTxHqyvSCpcE.ACRnQsNuTh1K_C9R.xpLNZ8Cc9faKoOYhss1CD0A4hG4m0M7-LZQ0fISw7NUHwzQs2AEo9ZXfwOvAj1fCbcE96mbKQo8gr7Oq1a2-piYXM1X5yNMcCxEaYyGinpnf6PGqbdr6zbYZdqyJk0KrxWVhKSQchLJaLGJOts4GlpqujSqJObJQcWWbkJQYKG9K7oKsdtMAKsHIVo5-0BCUbjKVnHJNsYwTsI7xn2Om8zGm4A.nBOuiEDssVFHC_N68tDjVA" -H "X-SAL-ContentType: e7FDDltrTy+tA2HnLovvGL0LFMwT+KkEptGju5wXVTU=" -H "DNT: 1" --compressed

"""

df_missouri_qtr_ann = df_missouri[df_missouri['form'].isin(['10-Q', '10-K'])]

df_missouri['instance'].apply(lambda x: x.split("-"))

df_microsoft = df_sub[df_sub['name'].str.contains('COCA COLA CO', regex=True)]

microsoft_adsh = df_microsoft.adsh.to_list()[0]

df_pre = pd.read_csv(data_file.open('pre.txt'), sep='\t', error_bad_lines=False)
df_num = pd.read_csv(data_file.open('num.txt'), sep='\t', error_bad_lines=False)
df_pre.head(100)

df_ko_num = df_num[df_num['adsh'].isin(['0000021344-19-000034'])]
df_revenues = df_num[df_num['tag'].str.contains('Revenues', regex=True)]
df_revenues.sort_values('adsh').head(100)

df_microsoft_num.sort_values("tag").drop_duplicates(subset=['tag'])
df_microsoft_num = df_microsoft_num[df_microsoft_num['form'].isin(['10-Q', '10-K'])]


df_ = df_.iloc[:, 0:len(df_.columns.tolist()[0:len(df_head.columns.tolist())])]
df_.columns = df_head.columns.to_list()

