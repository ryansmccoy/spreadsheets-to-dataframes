CREATE TYPE US_STOCK AS ENUM (
'AAPL','AMZN','GOOGL','MSFT',
'FB','BABA','BRK.B','JPM',
'XOM','JNJ','V','BAC','WFC',
'WMT','UNH','INTC','T','CVX',
'HD','PFE','VZ','MA','CSCO','PG',
'BA','KO','ORCL','NFLX','C','MRK',
'DIS'
);

CREATE TABLE stock (
    pk SERIAL,
    symbol US_STOCK,
    valid_until TIMESTAMP WITH TIME ZONE,
    price DECIMAL,
    CONSTRAINT pk PRIMARY KEY (pk, symbol, valid_until)
);
