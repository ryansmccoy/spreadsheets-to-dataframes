import pandas as pd

filepath = r'2019-11-04T00-02-57_stlregionalchamber_largest_employers.csv'

df = pd.read_csv(filepath)
df.columns = df.columns.str.strip().to_list()
df.columns = df.columns.str.replace(" ","_")
df.columns = df.columns.str.replace("(","_").str.replace(")","_")
df.columns = df.columns.str.lower()

df_nan = df[df.website.isna()]
df = df.dropna(subset=['website'])

df['website'] = df.website.str.replace('www.',"")
df['website'] = df['website'].apply(lambda x : "https://" + x)

import tldextract

folderpath = r'D:\PROJECTS\presentations\stl_data'

import glob

files = glob.glob(folderpath + "\\*.csv")

import os

df_list = []
for file in files:
    df = pd.read_csv(file)
    df['year'] = os.path.basename(file).split("_")[0]
    df_list.append(df)

df = pd.concat(df_list)

df.columns = df.columns.str.strip().to_list()
df.columns = df.columns.str.replace(" ","_")
df.columns = df.columns.str.replace("(","_").str.replace(")","_")
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(".","")

df = df.dropna(subset=['website'])
df['website'] = df.website.str.replace('www.',"")
df['website'] = df['website'].apply(lambda x : "https://" + x)
df.sort_values('st_louis_employees', ascending=False)
df['st_louis_employees'] = df.st_louis_employees.astype(int)
df['website_domain'] = df['website'].apply(lambda x: tldextract.extract(x).domain)

df_groups = []

for i, df_group in df.groupby('website_domain'):
    if df_group.index.size > 1:
        df_group = df_group.sort_values('year')
        df_group['pct_chg'] = df_group['st_louis_employees'].pct_change()
    else:
        df_group['pct_chg'] = None

    df_groups.append(df_group)

df_all = pd.concat(df_groups)
df_all.sort_values('st_louis_employees', ascending=False)
