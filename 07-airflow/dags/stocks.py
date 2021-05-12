# import json
# from datetime import datetime, timedelta
#
# import redis
# from airflow.models import DAG
# from airflow.operators import PythonOperator
#
# stocks = ('AAPL', 'AMZN', 'GOOGL', 'MSFT',
#           'FB', 'BABA', 'BRK.B', 'JPM',
#           'XOM', 'JNJ', 'V', 'BAC', 'WFC',
#           'WMT', 'UNH', 'INTC', 'T', 'CVX',
#           'HD', 'PFE', 'VZ', 'MA', 'CSCO', 'PG',
#           'BA', 'KO', 'ORCL', 'NFLX', 'C', 'MRK',
#           'DIS')
#
#
# def get_stocks(ds, **context):
#     symbol = context['params']['symbol']
#
#     pg_hook = postgres_hook(postgres_conn_id='stocks')
#     api_hook = http_hook(http_conn_id='alphavantage', method='GET')
#
#     # If either of these raises an exception then we'll be notified via
#     # Airflow
#     resp = api_hook.run(f'query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey=537201H9R203WT4C&datatype=csv')
#     resp = json.loads(resp.content)
#
#     # These are the only valid stocks the DB supports at the moment. Anything
#     # else that turns up will be ignored.
#
#     stocks_insert = f"""INSERT INTO stocks (symbol, valid_until, price)
#                       VALUES ({symbol}, {valid_until}, {price});"""
#
#     # If this raises an exception then we'll be notified via Airflow
#     valid_until = datetime.fromtimestamp(resp['timestamp'])
#
#     for iso2, price in resp['stocks'].items():
#         # If converting the price to a float fails for whatever reason then
#         # just move on.
#         try:
#             price = float(price)
#         except:
#             continue
#
#         iso2 = iso2.upper().strip()
#
#         if iso2 not in stocks or price < 0:
#             continue
#
#         pg_hook.run(stocks_insert, parameters=(iso2,
#                                                valid_until,
#                                                price))
#
#
# def cache_latest_stocks(ds, **kwargs):
#     redis_conn = redis.StrictRedis(host='redis')
#     pg_hook = postgres_hook(postgres_conn_id='stocks')
#     latest_stocks = """SELECT DISTINCT ON (symbol)
#                              symbol, price
#                       FROM   stocks
#                       ORDER  BY symbol, valid_until DESC;"""
#
#     for iso2, stock in pg_hook.get_records(latest_stocks):
#         redis_conn.set(iso2, stock)
#
#
# args = {
#     'owner': 'ryan',
#     'depends_on_past': False,
#     'start_date': datetime.utcnow(),
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }
#
# # Run at the top of the hour Monday to Friday.
# # Note: This doesn't line up with the market hours of
# # 10PM Sunday till 10PM Friday GMT.
# dag = DAG(dag_id='stocks',
#           default_args=args,
#           schedule_interval='0 * * * 1,2,3,4,5',
#           dagrun_timeout=timedelta(seconds=30))
#
# # loop through the lob's we want to use to build up our dag
# for stock in stocks:
#     get_stocks_task = \
#         PythonOperator(task_id='get_stocks',
#                        provide_context=True,
#                        op_kwargs={"stock": stock},
#                        python_callable=get_stocks,
#                        dag=dag)
#
#     cache_latest_stocks_task = \
#         PythonOperator(task_id='cache_latest_stocks',
#                        provide_context=True,
#                        python_callable=cache_latest_stocks,
#                        dag=dag)
#
#     get_stocks_task.set_downstream(cache_latest_stocks_task)
