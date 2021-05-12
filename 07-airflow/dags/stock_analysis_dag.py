from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from datetime import datetime, timedelta
import datetime as dt
import pandas as pd
import yfinance as yf
import requests

from functools import reduce


############################################
# DEFINE AIRFLOW DAG (SETTINGS + SCHEDULE)
############################################
default_args = {
     'owner': 'airflow',
     'depends_on_past': False,
     'email': ['user@gmail.com'],
     'email_on_failure': False,
     'email_on_retry': False,
     'retries': 1
    }

dag = DAG( 'stocks_analysis_ETL_7AM',
            default_args=default_args,
            description='Collect Stock Prices For Analysis',
            catchup=False,
            start_date= datetime(2020, 6, 23),
            schedule_interval= '* 7 * * *'
          )

tickers = ['AAPL', 'AMZN', 'BLK', 'T', 'TSLA'] # <-- Initial Tickers List. It will be available globally for all functions.

####################################################
# DEFINE PYTHON FUNCTIONS
####################################################

def fetch_prices_function(**kwargs): # <-- Remember to include "**kwargs" in all the defined functions
    print('1 Fetching stock prices and remove duplicates...')
    stocks_prices = []
    for i in range(0, len(tickers)):
        prices = yf.download(tickers[i], period = 'max').iloc[: , :5].dropna(axis=0, how='any')
        prices = prices.loc[~prices.index.duplicated(keep='last')]
        prices = prices.reset_index()
        prices.insert(loc = 1, column = 'Stock', value = tickers[i])
        stocks_prices.append(prices)
    return stocks_prices  # <-- This list is the output of the fetch_prices_function and the input for the functions below


def stocks_plot_function(**kwargs):
    print('2 Pulling stocks_prices to concatenate sub-lists to create a combined dataset + write to CSV file...')
    ti = kwargs['ti']
    stocks_prices = ti.xcom_pull(task_ids='fetch_prices_task')  # <-- xcom_pull is used to pull the stocks_prices list generated above
    stock_plots_data = pd.concat(stocks_prices, ignore_index=True)
    stock_plots_data.to_csv('/Users/anbento/Documents/Data_Sets/Medium/stocks_plots_data.csv', index=False)

    print('DF Shape: ', stock_plots_data.shape)
    print(stock_plots_data.head(5))
    print('Completed \n\n')

def stocks_table_function(**kwargs):
    print('3 Creating aggregated dataframe with stock stats for last available date + write to CSV file...')
    ti = kwargs['ti']
    stocks_prices = ti.xcom_pull(task_ids='fetch_prices_task') # <-- xcom_pull is used to pull the stocks_prices list generated above
    stocks_adj_close = []
    for i in range(0, len(stocks_prices)):
        adj_price= stocks_prices[i][['Date','Adj Close']]
        adj_price.set_index('Date', inplace = True)
        adj_price.columns = [tickers[i]]
        stocks_adj_close.append(adj_price)

    stocks_adj_close = reduce(lambda left,right: pd.merge(left, right, left_index = True, right_index = True ,how='outer'), stocks_adj_close)
    stocks_adj_close.sort_index(ascending = False, inplace = True)
    stocks_adj_close.index = pd.to_datetime(stocks_adj_close.index).date

##########################################
# DEFINE AIRFLOW OPERATORS
##########################################

fetch_prices_task = PythonOperator(task_id = 'fetch_prices_task',
                                   python_callable = fetch_prices_function,
                                   provide_context = True,
                                   dag= dag )

stocks_plot_task= PythonOperator(task_id = 'stocks_plot_task',
                                 python_callable = stocks_plot_function,
                                 provide_context = True,
                                 dag= dag)

stocks_table_task = PythonOperator(task_id = 'stocks_table_task',
                                  python_callable = stocks_table_function,
                                  provide_context = True,
                                  dag= dag)

##########################################
# DEFINE TASKS HIERARCHY
##########################################

fetch_prices_task  >> stocks_plot_task >> stocks_table_task
