import streamlit as st
import requests
from requests.auth import HTTPBasicAuth
import json
import re
import pandas as pd

## Title header
html_temp = """
<div style="background-color:lightgreen;padding:1px;">
<h1><center> Streamlit app</center></h1>
</div>
"""



st.markdown(html_temp, unsafe_allow_html=True)
st.write('')
st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}body{background-color: lightgreen;}
</style>
""",
    unsafe_allow_html=True,
)

access_token =''
inputUri= "s3://edgardataset/raw_layer/"
outputUri= "s3://edgardataset/masked/"

if st.sidebar.button('Generate Token'):
    headers = {  'Content-Type': 'application/x-www-form-urlencoded',}
    params = (   ('grant_type', 'client_credentials'),    )
    response = requests.post('https://team5-csye7245.auth.us-east-1.amazoncognito.com/oauth2/token', headers=headers, params=params, auth=('114525gkm76uvtvgtqlu91mlus', 'mp1s243oodd3vhba68du8ogj2onbd4qmjr4ok20g2trgnjmqib3'))

    st.write("Access Token: ",re.split("\"", response.text)[3])
    st.write("Token generated")
    ## Set access token
    access_token = re.split("\"", response.text)[3]


## define URL
url1 = "https://i4q6ts5eic.execute-api.us-east-1.amazonaws.com/team_5_134/api-1"
url2 = "https://i4q6ts5eic.execute-api.us-east-1.amazonaws.com/team_5_134/api-2"
url3 = "https://i4q6ts5eic.execute-api.us-east-1.amazonaws.com/team_5_134/api-3"
#st.write("AccessToken: ",access_token)
headers = {'Accept': 'application/json', 'Authorization': 'eyJraWQiOiJIZzJDZDdYRzFFc3FQaWltU1NjcjRqUXBZcHVUXC81MTNpc3V4VW9DOUNWUT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMTQ1MjVna203NnV2dHZndHFsdTkxbWx1cyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoidGVhbTUtY3N5ZTcyNDUtc2VydmVyLWlkXC9sYW1iZGEtaW52b2tlIiwiYXV0aF90aW1lIjoxNjE4NTk4OTYxLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9mRFFoVTBKaWEiLCJleHAiOjE2MTg2ODUzNjEsImlhdCI6MTYxODU5ODk2MSwidmVyc2lvbiI6MiwianRpIjoiZWEwNzYyNTAtMzRiNC00ZWNiLWJhMmQtM2ViMmVmMmM5NzA3IiwiY2xpZW50X2lkIjoiMTE0NTI1Z2ttNzZ1dnR2Z3RxbHU5MW1sdXMifQ.dpFAVRdPLkgfv72I_3IILrkX4ctNSPjYGLv4m8aduvSs3wl8aKXtSzsC0uJz1twV7f-f5jL_8CNSLt3YWutRPAkAB4nEBZFQUlpiGB_XBmdLPKLaWvRbhDQrcAATV43sw0V64Z3zH7fHfAn6Lsz0aROj1GZQlM548pCWUWdNnzrQpyWBlwI0xHgeOnyGYd6b2qs7SfHLRuDvi2Gkj9YDxMDxdnL05NayUEovty9M8YkiuAunll6JDJ9O8Cy4ylOpEMfodYL7C6bjADb7YKEVJLJSLYkKZ98dhoCZZ2wf0ad-4EzyPNJzgczWIN5MMT1ChElECEc4JlbATUZj-UV6gw'}

## select companies
company = st.sidebar.selectbox("Select company:", 
                                                 ['-------- Select --------',
                                                  'AGEN',
                                                  'ALTG',
                                                  'AXU',
                                                  'CALA',
                                                  'DAL',
                                                  'DD',
                                                  'ENLAY',
                                                  'FDX',
                                                  'GOL',
                                                  'JBL',
                                                  'NKE',
                                                  'PD',
                                                  'SBUX',
                                                  'TITN',
                                                  'UTZ',
                                                  'VOLT',
                                                  'WB',
                                                  'XOG'
                                                  ], index = 0
                                                 )

## select encryption
encryption = st.sidebar.selectbox("Select level of encryption",
                                  ['---- Select ---',
                                  'Raw data',
                                  'Anonymized',
                                  'Masked'],
                                  index = 0
                                  )

if 'Select' in company:
    st.write('Please select a company.')
else:
    if encryption == 'Raw data':
        st.write('API1 Raw Data')
        st.write('The selected company: ' + company)
        params = {"tag": company}
        req = requests.get(url1, headers=headers , params=params)
        j = json.loads(req.text)
        st.write(json.dumps(j))
    elif encryption == 'Anonymized':
        st.write('API2 Anonymized Data')
        st.write('The selected company: ' + company)
        params = {"tag": company}
        req = requests.get(url2, headers=headers , params=params)
        j = json.loads(req.text)
        st.write(json.dumps(j))
    elif encryption == 'Masked':
        st.write('API3 Masked Data')
        params = {"inputUri": 's3://edgardataset/raw_layer/AGEN/', "outputUri":'s3://edgardataset/masked/'}
        req = requests.get(url3, headers=headers , params=params)
        j = json.loads(req.text)
        st.write(json.dumps(j))
    else:
        st.write('Please select a level of encryption.')
        
## Load sentiment Analysis file
# sent = pd.read_csv(r'C:\Users\Win10\Downloads\_data.csv', header=None, names=['Text', 'Sentiment_Score'])
# sent.Sentiment_Score = [t.replace( '[', '') for t in sent.Sentiment_Score]
# sent.Sentiment_Score = [t.replace( ']', '') for t in sent.Sentiment_Score]
# sent.Sentiment_Score = sent.Sentiment_Score.astype(float)
# sent['sentiment'] = ['Positive' if t >= 0.6 else 'Neutral' if 0.3 < t < 0.6 else 'Negative' for t in sent.Sentiment_Score]
# st.write(sent)
    
    
    
    
    
    