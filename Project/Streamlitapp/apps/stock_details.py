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
import tensorflow as tf 
from sklearn.preprocessing import MinMaxScaler
import boto3

api_key = 'HN3A9YZW181QU71F'

def app():
    header_html1 = "<p style='text-align-last:center;font-size: 2rem'>Stocks Analysis</p>"
    st.markdown(
        header_html1, unsafe_allow_html=True,
    )
    list_symbols = []
    @st.cache
    def get_rawData():
        s3 = boto3.client('s3', 
                  region_name='us-east-1') 

        obj = s3.get_object(Bucket= 'lstmmodel', Key= 'listcompanies/listcompanies.csv') 

        rawData = pd.read_csv(obj['Body'])
        return rawData
    
    def get_company_overview(company_name):
        overview_url_string = "https://www.alphavantage.co/query?function=OVERVIEW&symbol=%s&apikey=%s"%(company_name,api_key)
        response = requests.get(overview_url_string).json()
        return response
    
    def get_graphs():
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
        
        
    def get_prediction_graphs():
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
        
        high_prices = df.loc[:,'High'].values
        low_prices = df.loc[:,'Low'].values
        mid_prices = (high_prices+low_prices)/2.0

        train_len = int(len(mid_prices)*0.7)
        #test_len = len(mid_prices) - int(len(mid_prices)*0.7)

        #print(train_len, test_len)

        train_data = mid_prices[:train_len]
        test_data = mid_prices[train_len:]
        scaler = MinMaxScaler()
        train_data = train_data.reshape(-1,1)
        test_data = test_data.reshape(-1,1)

        smoothing_window_size = 2500
        for di in range(0,len(train_data),smoothing_window_size):
            scaler.fit(train_data[di:di+smoothing_window_size,:])
            train_data[di:di+smoothing_window_size,:] = scaler.transform(train_data[di:di+smoothing_window_size,:])
            
        train_data = train_data.reshape(-1)

        # Normalize test data
        test_data = scaler.transform(test_data).reshape(-1)    
        
        EMA = 0.0
        gamma = 0.1
        for ti in range(len(train_data)):
          EMA = gamma*train_data[ti] + (1-gamma)*EMA
          train_data[ti] = EMA

        # Used for visualization and test purposes
        all_mid_data = np.concatenate([train_data,test_data],axis=0)
        
        window_size = 100
        N = train_data.size
        std_avg_predictions = []
        std_avg_x = []
        mse_errors = []

        for pred_idx in range(window_size,N):

            if pred_idx >= N:
                date = dt.datetime.strptime(k, '%Y-%m-%d').date() + dt.timedelta(days=1)
            else:
                date = df.loc[pred_idx,'Date']

            std_avg_predictions.append(np.mean(train_data[pred_idx-window_size:pred_idx]))
            mse_errors.append((std_avg_predictions[-1]-train_data[pred_idx])**2)
            std_avg_x.append(date)
        
        plt.figure(figsize = (18,9))
        plt.plot(range(df.shape[0]),all_mid_data,color='b',label='True')
        plt.plot(range(window_size,N),std_avg_predictions,color='orange',label='Prediction')
        #plt.xticks(range(0,df.shape[0],50),df['Date'].loc[::50],rotation=45)
        plt.xlabel('Date')
        plt.ylabel('Mid Price')
        plt.legend(fontsize=18)
        plt.show()
        st.pyplot()
        
        
        window_size = 100
        N = train_data.size

        run_avg_predictions = []
        run_avg_x = []

        mse_errors = []

        running_mean = 0.0
        run_avg_predictions.append(running_mean)

        decay = 0.5

        for pred_idx in range(1,N):

            running_mean = running_mean*decay + (1.0-decay)*train_data[pred_idx-1]
            run_avg_predictions.append(running_mean)
            mse_errors.append((run_avg_predictions[-1]-train_data[pred_idx])**2)
            run_avg_x.append(date)
            
        plt.figure(figsize = (18,9))
        plt.plot(range(df.shape[0]),all_mid_data,color='b',label='True')
        plt.plot(range(0,N),run_avg_predictions,color='orange', label='Prediction')
        #plt.xticks(range(0,df.shape[0],50),df['Date'].loc[::50],rotation=45)
        plt.xlabel('Date')
        plt.ylabel('Mid Price')
        plt.legend(fontsize=18)
        plt.show()
        st.pyplot()

    
    if not list_symbols:
        rawData = get_rawData() 
        list_symbols = rawData['symbol'].tolist()
        list_symbols.insert(0, "Select a Company")
           
    
    company = st.sidebar.selectbox("Select company:", list_symbols, index = 0)
    companyname = ''
    if not companyname:
        companyname = rawData.loc[rawData['symbol'] == company, 'name'].to_string(header=False, index=False)
    
    encryption = st.sidebar.selectbox("Select task",
                                  ['---- Select ---',
                                  'Get Details',
                                  'Get Graphs',
                                  'Get Predictions'],
                                  index = 0
                                  )
    if 'Select' in company:
        header_html3 = "<p style='text-align-last:center;font-size: 1rem;padding: 10px; border: 1px solid rgba(50, 147, 168, 0.2);background-color:rgba(50, 147, 168, 0.2)'>Please select a company</p>"
        st.markdown(
            header_html3, unsafe_allow_html=True,
        )
    
    else:
        if company != 'Select a Company':

            st.success('Selected Company: '+companyname)
            if encryption == 'Get Details':  
                company_response = get_company_overview(company)
                st.write(company_response)
            if encryption == 'Get Graphs':  
                get_graphs()
            if encryption == 'Get Predictions':  
                get_prediction_graphs()
    
    
        
