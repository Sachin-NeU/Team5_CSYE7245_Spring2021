import streamlit as st
from sklearn import datasets
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import urllib.request, json
import os
import numpy as np
import requests
import io

def app():
    api_key = 'HN3A9YZW181QU71F'
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title('Stocks')

    url_string = "https://www.alphavantage.co/query?function=LISTING_STATUS&apikey="+api_key
    response = requests.get(url_string)
    r = response.content
    rawData = pd.read_csv(io.StringIO(r.decode('utf-8'))) 
    listsymbols = rawData['symbol'].tolist()
    listsymbols.insert(0, "Select a Company")
    listcompanies = rawData['name'].tolist()
    ## select companies
    company = st.sidebar.selectbox("Select company:", listsymbols, index = 0)
    
    

    if company != 'Select a Company':
        st.write('The selected company: ' + company)
        url_string = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&outputsize=full&apikey=%s"%(company,api_key)
        with urllib.request.urlopen(url_string) as url:
            data = json.loads(url.read().decode())
            # extract stock market data
            data = data['Time Series (Daily)']
            df = pd.DataFrame(columns=['Date','Low','High','Close','Open'])
            for k,v in data.items():
                date = dt.datetime.strptime(k, '%Y-%m-%d')
                data_row = [date.date(),float(v['3. low']),float(v['2. high']),
                            float(v['4. close']),float(v['1. open'])]
                df.loc[-1,:] = data_row
                df.index = df.index + 1  
        
        df = df.sort_values('Date')

     
        
        plt.figure(figsize = (15,8))
        plt.plot(range(df.shape[0]),(df['Low']+df['High'])/2.0)
        plt.xticks(range(0,df.shape[0],500),df['Date'].loc[::500],rotation=45)
        plt.xlabel('Date',fontsize=18)
        plt.ylabel('Mid Price',fontsize=18)
        plt.show()    
        st.pyplot()
