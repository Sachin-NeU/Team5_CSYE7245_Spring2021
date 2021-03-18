### FastAPI


#### Requirements

```
pip3 install fastapi
pip3 install uvicorn
pip3 install iexfinance
```

#### Getting Started

Basic usage is available in `main.py`. Run the server with `uvicorn main:app --reload`. 
Go to `http://127.0.0.1:8000/docs` and you should see the interactive API documentation.

#### Stock Market Prices

Building an API for brokerage to keep a track of investors buying and selling on the stock-market, using their website/app. 
In addition to serving `PUT` and `GET` requests, the endpoint stores all data on DynamoDB.

Create a table on DynamoDB with `id` as the primary key before running the server.

- `stock_price.py` - A simple Python script to get the current stock price of a given company. This requires an API token to query IEX Cloud and fetch the current stock price. Create a free developer account [here](https://iexcloud.io/). Once you have the account, go to `Home > API Tokens` and copy the `SECRET` token, and use your token in the `stock_price.py` script. 

- `id_generator.py` - Python script to generate a unique 10 digit alpha-numeric ID

- `trades.py` - Script to deploy the FastAPI endpoint. Use the created DynamoDB table in this script. Contains three routes:


Fetch the price of a given stock:
```
# Get the current stock price
@app.get("/stock_price/{name}")
```

Place Trades - Required params: `customer_id, name, qty, position`

```
# Place trades
@app.put("/trade/{customer_id}")
```

Get all trades for a given customer ID - Required params: `customer_id`
```
@app.get("/get_trades/{customer_id}")
```

Run the server with `uvicorn trades:app --reload`. Go to `http://127.0.0.1:8000/docs` and you should see the interactive API documentation.

CLAAT Document :- https://docs.google.com/document/d/1pUdpgLh65cAvLfpnmDwwBEtp6LB7FI0t5ZdWI-h2gHs/edit?usp=sharing
