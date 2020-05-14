
### Deployment

1. Create a persistent docker volume for postgresql: docker volume create --name airflow-postgresql -d local
2. Clone the git repository and fire up the containers: docker-compose up -d
3. Go to http://localhost:8080
4. Add connection under Admin -> Connections
	* A connection type of Postgres
	* A connection identifier of rates
	* A host string of postgres (the postgresql service name, see docker-compose.yml)
	* A schema string (database name) of airflow
	* A login of username=airflow and password=airflow
5. Add connection under Admin -> Connections
	* A connection type of HTTP
	* A connection identifier of alphavantage
	* A host string of the full API endpoint:     https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey=537201H9R203WT4C&datatype=csv

$ sudo apt update
$ sudo apt install \
    libffi-dev \
    libmysqlclient-dev \
    mysql-server \
    postgresql-9.3 \
    postgresql-server-dev-9.3 \
    python-dev \
    python-pip \
    python-virtualenv \
    rabbitmq-server \
    redis-server

$ sudo apt update
$ sudo apt-get install \
    libffi-dev \
    libmysqlclient-dev \
    python3-dev \
    mysql-server \
    python3-pip \
    python3-virtualenv \
    redis-server

$ sudo su - postgres -c \
    "createuser \
        --pwprompt \
        --superuser \
        ryan"
        
$ createdb stocks

$ mysql \
    -uroot \
    -proot \
    -e "CREATE DATABASE airflow
        DEFAULT CHARACTER SET utf8
        DEFAULT COLLATE utf8_general_ci;

        GRANT ALL PRIVILEGES
        ON airflow.*
        TO 'airflow'@'localhost'
        IDENTIFIED BY 'airflow';

        FLUSH PRIVILEGES;"
        
sudo /etc/init.d/redis-server start

$ virtualenv .env
$ source .env/bin/activate

$ pip install apache-airflow[postgres] \
    celery \
    cryptography \
    redis

$ airflow initdb

$ airflow webserver

$ open http://127.0.0.1:8080/admin/connection/
