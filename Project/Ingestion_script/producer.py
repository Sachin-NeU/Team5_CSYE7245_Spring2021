import boto3
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class TweetStreamListener(StreamListener):
    # on success
    def on_data(self, data):

        # decode json
        tweet = json.loads(data)
        print(tweet)
        # print(tweet)
        if "text" in tweet.keys():
            payload = {'id': str(tweet['id']),
                       'tweet': str(tweet['text']),
                       'ts': str(tweet['created_at'])
                       }
            print(type(payload))

            if not(payload['tweet'].startswith('RT')):
                print(payload)
                try:
                    put_response = kinesis_client.put_record(
                        StreamName=stream_name,
                        Data=json.dumps(payload),
                        PartitionKey=str(tweet['user']['screen_name']))
                    print(put_response)
                except (AttributeError, Exception) as e:
                    print(e)
                    pass
        return True

    # on failure
    def on_error(self, status):
        print(status)


stream_name = 'TSLA'  # fill the name of Kinesis data stream you created
query = ['#TSLA','Elon','TESLA']
consumer_key = 'f6sxSv3IkOnEyNIwF9Ycayf6i'
consumer_secret = 'mvVQNtYGDDe5Tv3T3Wwa5SL1GYaqY9PFow91m4jSs0t7bbtltV'
access_token = '3166578447-hoMCQrwmdoeJRj14aoPIwj2G7hWINgdvAmkOv9F'
access_token_secret = 'FndXsZ7REb8PekqUZMwaxRtHU2ubj3W8Xk9RmoaPGyWsV'

if __name__ == '__main__':
    # create kinesis client connection
    kinesis_client = boto3.client('kinesis',region_name='us-east-1')  # fill you aws secret access key

    # create instance of the tweepy tweet stream listener
    listener = TweetStreamListener()

    # set twitter keys/tokens
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # create instance of the tweepy stream
    stream = Stream(auth, listener)

    # search twitter for tags or keywords from cli parameters
    print(query)

    stream.filter(track=query,languages=['en'])