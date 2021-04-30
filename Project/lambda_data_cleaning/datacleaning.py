import boto3
import re
import emoji
import json
import string
import random


def lambda_handler(event=None, context=None):
    #def removeStopwords(contents):

        # nltk.download('words')
        # words = set(nltk.corpus.words.words())
        # tweet = " ".join(w for w in nltk.wordpunct_tokenize(contents) \
        #                 if w.lower() in words or not w.isalpha())
        # nlp = English()
        #
        # my_doc = nlp(contents)
        #
        # token_list = []
        # for token in my_doc:
        #     token_list.append(token.text)
        #
        # filtered_sentence_string = ""
        #
        # for word in token_list:
        #     lexeme = nlp.vocab[word]
        #     if not lexeme.is_stop:
        #         filtered_sentence_string = filtered_sentence_string + " " + word

        #return tweet

    def removePunctuation(contents):
        punc_removed_string = re.sub(r'[^\w\s.]', '', contents)
        spaces_removed_string = " ".join(punc_removed_string.split())
        return spaces_removed_string


    def cleaner(tweet):
        tweet = removePunctuation(tweet)  # Remove @ sign

        tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet)  # Remove http links

        tweet = " ".join(tweet.split())

        tweet = ''.join(c for c in tweet if c not in emoji.UNICODE_EMOJI)  # Remove Emojis

        tweet = tweet.replace("#", "").replace("_", " ")  # Remove hashtag sign but keep the text

        # tweet = removeStopwords(tweet)

        return tweet



    bucket_name = 'stockpriceteam5'
    s3_client = boto3.client('s3')
    kwargs = {'Bucket': bucket_name, 'Prefix': "raw_layer/"}
    response = s3_client.list_objects_v2(**kwargs)
    all = response['Contents']
    latest = max(all, key=lambda x: x['LastModified'])
    latest_file = latest['Key']
    stock_split = latest_file.split('/')
    stock_location = '/'.join(stock_split[i] for i in range(1, len(stock_split) - 1))
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(bucket_name)
    result = {}
    result['data'] = []

    for object_summary in my_bucket.objects.filter(Prefix=latest_file):
        body = object_summary.get()['Body'].read()
        string_body = body.decode("utf-8")
        string_body = re.sub(r'\\n', " ", string_body)
        arr = string_body.split('2021"}')
        for i in arr:
            temp = i + '2021"}'
            try:
                temp_json = json.loads(temp)
                original_tweet = temp_json['tweet']
                ts = temp_json['ts']
                clean_tweet = cleaner(original_tweet)
                result['data'].append({
                    'tweet': original_tweet,
                    'clean_tweet': clean_tweet,
                    'ts':ts
                })
            except:
                pass

    print(result)
    letters = string.ascii_letters
    file = ''.join(random.choice(letters) for i in range(10))
    client = boto3.client('s3')
    bucket_name_destination = 'stockpriceteam5optimized'
    key = stock_location + '/' + file + '.txt'
    print(key)
    client.put_object(Body=str(result), Bucket=bucket_name_destination, Key=key)


lambda_handler()