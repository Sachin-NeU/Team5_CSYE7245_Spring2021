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
import datetime
from pytz import timezone

from tensorflow.keras.models import model_from_json

api_key = 'HN3A9YZW181QU71F'

st.set_option('deprecation.showPyplotGlobalUse', False)
def app():    
    st.title('Our Prediction')
    list_symbols = []
    
    @st.cache
    def get_rawData():
        s3 = boto3.client('s3', 
                  region_name='us-east-1',
                  aws_access_key_id='AKIAQI43754RZCTWJJOX', 
                  aws_secret_access_key='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') 

        obj = s3.get_object(Bucket= 'lstmmodel', Key= 'listcompanies/listcompanies.csv') 

        rawData = pd.read_csv(obj['Body'])
        return rawData
        
    def get_stock_data(company):
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
        return df
    
    def get_realtime_tweets(company_tweet):
        s3 = boto3.client("s3", 
                  region_name='us-east-1'
                  )

        resource = boto3.resource('s3')
        today = str(datetime.date.today())
        
        datee = datetime.datetime.strptime(today, "%Y-%m-%d")
        current_month = str(datee.month)

        if int(current_month) > 9:
            current_month = current_month
        else:
            current_month = '0' + str(current_month)
            
        current_day = str(datee.day)
        if int(current_day) > 9:
            current_day = current_day
        else:
            current_day = '0' + str(current_day)
            
        current_year = str(datee.year)

        if int(current_year) > 9:
            current_year = current_year
        else:
            current_year = '0' + str(current_year)
            
        now = datetime.datetime.now()
        now_utc = datetime.datetime.now(timezone('UTC'))
        format = "%H"
        
        time_hour = now_utc.strftime(format)
        if int(time_hour) > 10:
            time_hour = time_hour
        else:
            time_hour = '0' + str(time_hour)
            
        my_bucket = resource.Bucket('stockpriceteam5business')
        
        path = company_tweet+'/year='+str(current_year)+'/month='+str(current_month)+'/day='+str(current_day)+'/hour='+str(time_hour)+'/'
        
        prefix = company_tweet+'/year='+str(current_year)+'/month='+str(current_month)+'/day='+str(current_day)+'/hour=00/'   
        
        df = pd.DataFrame(columns=['tweet', 'sentiment', 'sentiment_score','ts'])
        for obj in my_bucket.objects.filter(Prefix=prefix):    
            body = obj.get()['Body'].read()
            string_body = body.decode("utf-8")
            final_dictionary = eval(string_body)
            for i in final_dictionary['data']:
                df = df.append(i, ignore_index=True)
        df['ts']= pd.to_datetime(df['ts'])
        df = df.set_index('tweet')
        #df = df.drop(['clean_tweet'], axis=1)
        return df


    
    if not list_symbols:
        rawData = get_rawData() 
        list_symbols = rawData['symbol'].tolist()
        list_symbols.insert(0, "Select a Company")           
    
    company = st.sidebar.selectbox("Select company:", list_symbols, index = 0)
    
    
    if 'Select' in company:
        st.write('Please select a company.')
    
    else:
        companyname = ''
        if not companyname:
            companyname = rawData.loc[rawData['symbol'] == company, 'name'].to_string(header=False, index=False)
            
        if company != 'Select a Company':
        
            
            st.write('The selected company: ' + companyname)
            df = get_stock_data(company)
            # Sort DataFrame by date
            df = df.sort_values('Date')
            

            #MODEL
            st.write('LSTM Model')
            json_file = open('C:/Vivek/PDP/Team5_CSYE7245_Spring2021/Project/model/model.json', 'r')
            loaded_model_json = json_file.read()
            json_file.close()
            loaded_model = model_from_json(loaded_model_json)
            # load weights into new model
            loaded_model.load_weights("C:/Vivek/PDP/Team5_CSYE7245_Spring2021/Project/model/model.h5")
            
            #loaded_model.load_weights("C:/Vivek/PDP/Team5_CSYE7245_Spring2021/Project/model/model.h5")
            # Create a new dataframe with only the 'Close column 
            data = df.filter(['Close'])
            values = st.sidebar.slider('Select a range of values',0, data['Close'].shape[0], (0, (data['Close'].shape[0]-25)))
             
            # Convert the dataframe to a numpy array
            dataset = data.values
            # Get the number of rows to train the model on
            training_data_len = int(np.ceil( len(dataset) * .95 ))
             
            # Scale the data
             
            scaler = MinMaxScaler(feature_range=(0,1))
            scaled_data = scaler.fit_transform(dataset)    

            # Create the testing data set
            # Create a new array containing scaled values from index 1543 to 2002 
            test_data = scaled_data[training_data_len - 60:,:]
            # Create the data sets x_test and y_test
            x_test = []
            y_test = dataset[training_data_len:,:]
            
            for i in range(60,len(test_data)):
                x_test.append(test_data[i-60:i,0])

            # Convert the data to a numpy array
            x_test = np.array(x_test)
             
            # Reshape the data
            x_test = np.reshape(x_test,(x_test.shape[0], x_test.shape[1],1))
             
            # Get the models predicted price values 
            predictions = loaded_model.predict(x_test)
            predictions = scaler.inverse_transform(predictions)
             
            # Get the root mean squared error (RMSE)
            rmse = np.sqrt(np.mean(((predictions - y_test) ** 2)))
            rmse
             
            # Plot the data
            train = data[:training_data_len]
            valid = data[training_data_len:]
            valid['Predictions'] = predictions
            # Visualize the data
            plt.figure(figsize=(16,8))
            plt.title('Model')
            plt.xlabel('Date', fontsize=18)
            plt.ylabel('Close Price USD ($)', fontsize=18)
            plt.plot(train['Close'][-values[1]:])
            plt.plot(valid[['Close','Predictions']])
            plt.legend(['Train','Val','Predictions'], loc='lower right')
            #plt.xticks(np.arange(0,4000, 300), df['Date'][0:4000:300])
            plt.xticks(np.arange(values[0],values[1],20), df['Date'][values[0]:values[1]:20])
            
            plt.show()


            st.pyplot()
            result = get_realtime_tweets(company)
            st.table(result)
    
   