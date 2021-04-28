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
import re
from spacy.lang.en import English
import boto3
import emoji
import nltk
nltk.download('words')
words = set(nltk.corpus.words.words())
import tweepy as tw


def app():
    st.title('Twitter')
    
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
        session = boto3.Session(
        aws_access_key_id='AKIAQI43754RXAMPRMNJ',
        aws_secret_access_key='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',
        )
        s3 = session.resource('s3')
        bucket_name = 'edgarpipeline'
        my_bucket = s3.Bucket(bucket_name)
        output = ""

        for object_summary in my_bucket.objects.filter(Prefix="2021/04/27/23/"):
            body = object_summary.get()['Body'].read()
            output = output + (str(body))
        #print (output)
        return output



    contents = connect_to_aws()
    
    #st.write(contents)
    hashtag = st.text_area("*Enter any keyword to get data from twitter*")
    
    if st.button("Show Data"):
       st.success("Fetching Tweets")           
       recent_tweets= get_tweets(hashtag)
       recent_tweets.reset_index(drop=True, inplace=True)
       st.table(recent_tweets)

        
