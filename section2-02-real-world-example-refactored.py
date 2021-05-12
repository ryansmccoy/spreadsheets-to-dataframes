import glob
import os
import zipfile
import re  # regular expression

import requests

import pandas as pd

# fixes display of dataframes in Python Console
pd.set_option('display.float_format', lambda x: f'{x:.5f}')
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 600)

current_directory = os.getcwd()


def extract_zip_contents(filepath):
    zip_file_local_extract_path = filepath.replace(".zip", "")

    # create directory for zip files
    if os.path.exists(zip_file_local_extract_path):

        print("Folder already Exists!")

    else:
        try:

            z = zipfile.ZipFile(zip_file_local_extract_path)

            z.extractall(zip_file_local_extract_path)

            print("Extracting Contents: \t", zip_file_local_extract_path)
        except:
            print("Issue Extracting, Going to Skip :)")
            return None

    return zip_file_local_extract_path


def download_filings(start_year, end_year, output_directory):
    quarters = ['q1', 'q2', 'q3', 'q4']

    zip_filepaths = []

    for year in range(start_year, end_year):
        for quarter in quarters:

            url = rf'https://www.sec.gov/files/dera/data/financial-statement-data-sets/{year}{quarter}.zip'

            try:

                # we can get the filename (basename) of the url using basename
                basename = os.path.basename(url)

                print(basename)

                zip_file_local_filepath = os.path.join(output_directory, basename)

                print(zip_file_local_filepath)

                zip_filepaths.append(zip_file_local_filepath)

                if not os.path.exists(zip_file_local_filepath):

                    print(f"Downloading: \t{url}")

                    r = requests.get(url)

                    if r.status_code == 200:

                        print(f"Download Complete")

                        with open(zip_file_local_filepath, 'wb') as fd:
                            fd.write(r.content)

                    else:
                        print("Got an Error Code!")

                else:
                    print("It appears Zip File already exists", zip_file_local_filepath)

            except Exception as E:
                print("Error Downloading", url, E)

    return zip_filepaths


def transform_data(numbers_filepath, submissions_filepath, df_sic_list, df_symbol_cik, metric="Revenues", form_type='10-'):
    print("Transforming ", numbers_filepath)

    df_numbers = pd.read_csv(numbers_filepath, delimiter="\t")

    df_submissions = pd.read_csv(submissions_filepath, delimiter="\t")

    # convert sic to string
    df_submissions['sic'] = df_submissions['sic'].astype('Int64').astype('str')

    df_submissions = df_submissions[['adsh', 'cik', 'name', 'sic', 'countryba', 'stprba', 'fye', 'form', 'period', 'filed', 'instance']]

    df_symbol_cik['symbol'] = df_symbol_cik['symbol'].str.upper()

    # create list of dataframe column names
    submissions_columns = df_submissions.columns.tolist()

    # going to merge two dataframes into one
    df_submissions_symbols = pd.merge(df_submissions, df_symbol_cik)

    # merge sic codes onto submission dataframe
    df_submissions_symbols = pd.merge(df_submissions_symbols, df_sic_list, on="sic")

    # we can drop columns by name using drop
    df_submissions_symbols = df_submissions_symbols.drop(columns=['instance'])

    new_submissions_columns = ["symbol", "industry_title"] + submissions_columns

    df_submissions_symbols = df_submissions_symbols.reindex(columns=new_submissions_columns)

    df_submissions_symbols = df_submissions_symbols[df_submissions_symbols['form'].str.contains(form_type, flags=re.IGNORECASE, regex=True)]

    df_submission_numbers = pd.merge(df_numbers, df_submissions_symbols, left_on='adsh', right_on='adsh', how='inner')

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

    # Group by: split-apply-combine
    if metric:
        df_values = df_submission_numbers[df_submission_numbers['tag'].isin([metric])]
    else:
        df_values = df_submission_numbers.copy()

    df_values = df_values.dropna(subset=['value'])

    # only show companies with 4 quarters (1 year) worth of data
    df_values = df_values[df_values['qtrs'] == 4]
    df_values = df_values[(df_values['uom'] == "USD") | (df_values['uom'] == "EUR")]

    df_values = df_values.sort_values('ddate', ascending=True)

    group = []

    for (symbol, qtrs), df_group in df_values.groupby(["symbol", "qtrs"]):
        df_group['pct_change'] = df_group['value'].pct_change()
        group.append(df_group)

    df_values_pct = pd.concat(group)

    df_values_pct = df_values_pct.sort_values('ddate', ascending=False)

    print("Done Transforming ", numbers_filepath)

    return df_values_pct


def filter_ticker_list(df_submissions_symbols):
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

    df_companies = pd.DataFrame(pycon_sponsors)

    ticker_list_pycon_sponsors = df_companies['symbol'].tolist()

    df_selected_submissions = df_submissions_symbols[df_submissions_symbols['symbol'].isin(ticker_list_pycon_sponsors)]

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

    df_selected_submissions = df_selected_submissions.reindex(columns=new_submissions_columns)

    return df_selected_submissions


def main(start_year, end_year):
    url = 'https://www.sec.gov/include/ticker.txt'

    df_symbol_cik = pd.read_csv(url, delimiter="\t", names=['symbol', 'cik'])

    # standard industrial classification
    sic_url = r'https://www.sec.gov/info/edgar/siccodes.htm'
    # we can extract table from html by passing in url
    sics_tables = pd.read_html(sic_url)
    df_sic_list = sics_tables[0]

    # rename columns to lower, no spaces, and rename sic_code to sic
    df_sic_list.columns = df_sic_list.columns.str.lower().str.replace(" ", "_").str.replace("sic_code", "sic")

    # convert sic column to string
    df_sic_list['sic'] = df_sic_list['sic'].astype('Int64').astype('str')

    output_directory = os.path.join(current_directory, "zip-data")

    # create directory for zip files
    if os.path.exists(output_directory):
        print("Folder already Exists!")
    else:
        print("Folder doesn't exist")
        os.mkdir(output_directory)
        print("Created Directory!")

    zip_filepaths = download_filings(start_year, end_year, output_directory)

    zip_folders = []

    for zip_filepath in zip_filepaths:
        zip_folder = extract_zip_contents(zip_filepath)

        if zip_folder:
            zip_folders.append(zip_folder)

    # get list of all extracted files
    files = glob.glob(output_directory + "\\*\\*.*")

    num_files = [file for file in files if "num.txt" in file]
    sub_files = [file for file in files if "sub.txt" in file]

    pre_files = [file for file in files if "pre.txt" in file]
    tag_files = [file for file in files if "tag.txt" in file]
    readme_files = [file for file in files if "readme.htm" in file]

    num_files.sort(reverse=True)
    sub_files.sort(reverse=True)

    if len(num_files) == len(sub_files):
        sub_num_files = list(zip(sub_files, num_files))

        filings = []

        for sub_file, num_file in sub_num_files[1:5]:
            df_companies_pct_chg = transform_data(num_file, sub_file, df_sic_list, df_symbol_cik, metric="Revenues", form_type='10-')

            filings.append(df_companies_pct_chg)

        df_all_filings = pd.concat(filings)

        # df_all_filings = df_all_filings.dropna(subset=['pct_change'])

        # df_all_filings = df_all_filings[df_all_filings['pct_change'] > 0]
        #
        # df_all_filings = df_all_filings.drop_duplicates(keep='first', subset=['cik']).sort_values('value', ascending=False)

        df_all_filings.to_csv('all_filings.csv')


if __name__ == "__main__":
    start_year = 2020
    end_year = 2022

    main(start_year, end_year)
