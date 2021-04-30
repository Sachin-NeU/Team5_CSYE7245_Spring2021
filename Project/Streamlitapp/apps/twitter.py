import streamlit as st
from sklearn import datasets
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import urllib.request, json
import os
import numpy as np
import requests
import io
import re
from spacy.lang.en import English
import boto3
import emoji
import nltk
nltk.download('words')
words = set(nltk.corpus.words.words())
import tweepy as tw
from pytz import timezone

# HomePage styling
html_temp = """
<div style="background-color:#800000;padding:1px; border-radius: 30px;">
<h1><center style= "color:white;">Twitter App</style></center></h1>
</div>
"""
#st.markdown(html_temp, unsafe_allow_html=True)
st.write('')
st.markdown(
    """
<style>
.css-1l02zno {
    background-color:#2596be;
    background-attachment: fixed;
    flex-shrink: 0;
    height: 100vh;
    color:black;
    overflow: auto;
    padding: 5rem 1rem;
    position: relative;
    transition: margin-left 300ms ease 0s, box-shadow 300ms ease 0s;
    width: 21rem;
    z-index: 100;
    margin-left: 0px;
}
.css-145kmo2 {
    font-size: 1rem;
    color: white;
    margin-bottom: 0.4rem;
}
.css-1vbb94r {
    width: 100%;
    margin-bottom: 1rem;
    border-collapse: collapse;
    border-radius: 30px;
    background-color: white;
    font-weight: bold;
}
.css-hi6a2p {
    flex: 1 1 0%;
    width: 100%;
    padding: 3rem 1rem 10rem;
    max-width: 730px;
}
canvas{
    width:800px !important;
    height:420px !important;
}
.css-1wrcr25 {
    display: flex;
    flex-direction: row;
    -webkit-box-pack: start;
    place-content: flex-start;
    -webkit-box-align: stretch;
    align-items: stretch;
    position: absolute;
    inset: 0px;
    overflow: hidden;
}
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}body{background-color: lightgreen;
    font-family: "Times New Roman", Times, serif}
</style>
""",
    unsafe_allow_html=True,
)


def app():
    header_html1 = "<p style='text-align-last:center;font-size: 2rem'>Twitter Analysis</p>"
    st.markdown(
        header_html1, unsafe_allow_html=True,
    )
    
    topics = st.sidebar.selectbox("Select task",
                                  ['---- Select ---',
                                  'Get Tweets',
                                  'Get Sentiments'],
                                  index = 0
                                  )
    def get_tweets(keyword):

        consumer_key = 'f6sxSv3IkOnEyNIwF9Ycayf6i'
        consumer_secret = 'mvVQNtYGDDe5Tv3T3Wwa5SL1GYaqY9PFow91m4jSs0t7bbtltV'
        access_token = '3166578447-hoMCQrwmdoeJRj14aoPIwj2G7hWINgdvAmkOv9F'
        access_token_secret = 'FndXsZ7REb8PekqUZMwaxRtHU2ubj3W8Xk9RmoaPGyWsV'

        auth = tw.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tw.API(auth, wait_on_rate_limit=True)
        search_words = keyword + " -filter:retweets"
        tweets = api.search(q=search_words,
                      lang="en", tweet_mode="extended")
        #st.write(tweets) 
        df = pd.DataFrame([tweet.full_text for tweet in tweets], columns=['Tweets'])
        # st.write(df)   
        
        
        # def cleanTxt(text):
            # text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
            # text = re.sub('#', '', text) # Removing '#' hash tag
            # text = re.sub('RT[\s]+', '', text) # Removing RT
            # text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink					 
        # return text
            
        # df['Tweets'] = df['Tweets'].apply(cleanTxt)
        

        return df
    
    def cleaner(tweet):
        tweet = re.sub("@[A-Za-z0-9]+","",tweet) #Remove @ sign
        tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet) #Remove http links
        tweet = " ".join(tweet.split())
        tweet = ''.join(c for c in tweet if c not in emoji.UNICODE_EMOJI) #Remove Emojis
        tweet = tweet.replace("#", "").replace("_", " ") #Remove hashtag sign but keep the text
        tweet = " ".join(w for w in nltk.wordpunct_tokenize(tweet) \
             if w.lower() in words or not w.isalpha())
        return tweet


    def connect_to_aws():
        session = boto3.Session()
        s3 = session.resource('s3')
        bucket_name = 'edgarpipeline'
        my_bucket = s3.Bucket(bucket_name)
        output = ""

        for object_summary in my_bucket.objects.filter(Prefix="2021/04/27/23/"):
            body = object_summary.get()['Body'].read()
            output = output + (str(body))
        #print (output)
        return output

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
        
        
        
    if topics == 'Get Tweets':  
        contents = connect_to_aws()
        st.write('Please add tags you want to search:')
        #st.write(contents)
        hashtag = st.text_area("*Enter any keyword to get data from twitter*")        
        if st.button("Show Data"):
           st.success("Fetching Tweets")           
           recent_tweets= get_tweets(hashtag)
           recent_tweets.reset_index(drop=True, inplace=True)
           st.table(recent_tweets)
           
    elif topics == 'Get Sentiments':
        header_html4 = "<p style='text-align-last:center;font-size: 1rem;padding: 10px; border: 1px solid rgba(50, 147, 168, 0.2);background-color:rgba(50, 147, 168, 0.2)'>Please select a company for live streaming tweets</p>"

        st.markdown(
            header_html4, unsafe_allow_html=True,
        )
        company_tweet = st.selectbox("Select company",
                                  ['---- Select ---',
                                  'TSLA',
                                  'APPL',
                                  'FB',
                                  'MSFT','TWTR'],
                                  index = 0
                                  )
        result = get_realtime_tweets(company_tweet)
        dfinal = pd.DataFrame(columns=['NEGATIVE', 'POSITIVE', 'NEUTRAL'])
        negative = 0
        positive = 0
        neutral = 0
        for i in range(0, len(result['sentiment'])):
            
            if result['sentiment'][i] == 'NEGATIVE':         
                negative += 1
            elif result['sentiment'][i] == 'POSITIVE':
                positive += 1
            elif result['sentiment'][i] == 'NEUTRAL':
                neutral +=1    
        
        dfinal = dfinal.append({'NEGATIVE' : negative,
                    'POSITIVE' : positive,
                   'NEUTRAL' : neutral} , 
                    ignore_index=True)
        #st.button("Re-run")
        header_html3 = "<p style='text-align-last:center;font-size: 1rem;padding: 10px; border: 1px solid rgba(50, 147, 168, 0.2);background-color:rgba(50, 147, 168, 0.2)'>Sentiments Segregation</p>"
        st.markdown(
            header_html3, unsafe_allow_html=True,
        )
        st.table(dfinal)
        header_html5 = "<p style='text-align-last:center;font-size: 1rem;padding: 10px; border: 1px solid rgba(50, 147, 168, 0.2);background-color:rgba(50, 147, 168, 0.2)'>Tweets and Scores</p>"
        st.markdown(
            header_html5, unsafe_allow_html=True,
        )
        st.table(result)
        
        

        
