
import re
from spacy.lang.en import English
import boto3



def removePunctuation(contents):
    punc_removed_string = re.sub(r'[^\w\s.]', '', contents)
    spaces_removed_string = " ".join(punc_removed_string.split())
    return spaces_removed_string


def removeStopwords(contents):
    nlp = English()

    my_doc = nlp(contents)

    token_list = []
    for token in my_doc:
        token_list.append(token.text)

    filtered_sentence_string = ""

    for word in token_list:
        lexeme = nlp.vocab[word]
        if not lexeme.is_stop:
            filtered_sentence_string = filtered_sentence_string + " " + word

    return filtered_sentence_string


def connect_to_aws():
    s3 = boto3.resource('s3')
    bucket_name = 'edgarpipeline'
    my_bucket = s3.Bucket(bucket_name)
    output = ""

    for object_summary in my_bucket.objects.filter(Prefix="raw_layer/"):
        body = object_summary.get()['Body'].read()
        output = output + datacleaning(str(body))
    print (output)
    return output

def datacleaning(contents):
    stop_word_removed_string = removeStopwords(contents)
    output_string = removePunctuation(stop_word_removed_string)
    return output_string


contents = connect_to_aws()
client = boto3.client('s3')
client.put_object(Body=contents, Bucket='edgarpipeline', Key='optimized_layer/cleaned_file.txt')
