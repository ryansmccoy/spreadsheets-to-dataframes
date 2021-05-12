import datetime

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {"owner": "airflow"}

# create_stock_table, populate_stock_table, get_all_stocks are examples of tasks created by
# instantiating the Postgres Operator

with DAG(
        dag_id="postgres_operator_dag",
        start_date=datetime.datetime(2020, 2, 2),
        schedule_interval="@once",
        default_args=default_args,
        catchup=False,
) as dag:

    create_stock_table = PostgresOperator(
        task_id="create_stock_table",
        postgres_conn_id="postgres_default",
        sql="sql/stock_schema.sql"
    )

    populate_stock_table = PostgresOperator(
        task_id="populate_stock_table",
        postgres_conn_id="postgres_default",
        sql="sql/stock_insert.sql"
    )

    get_all_stocks = PostgresOperator(
        task_id="get_all_stocks", postgres_conn_id="postgres_default", sql="SELECT * FROM stocks;"
    )

    create_stock_table >> populate_stock_table >> get_all_stocks
