import requests
import json
from datetime import datetime
url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
"""
Banknifty:-https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY
Other Stock:-https://www.nseindia.com/api/option-chain-equities?symbol=ADANIENT
"""
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url,headers=headers,verify=False)
data = json.loads(page.text)
exp=datetime.strptime(data['records']['expiryDates'][0], '%d-%b-%Y')
import pandas as pd

data1=pd.DataFrame(data['records']['data'])
data1['expiryDate'] =  pd.to_datetime(data1['expiryDate'], format='%d-%b-%Y')

curr=int(data1.loc[0][2]['underlyingValue'])                #get current underlying value

data1.drop(data1[data1['expiryDate'] != exp.strftime('%x')].index, inplace = True)      #drop data which is not of latest expiery date

data1.drop(data1[data1['strikePrice']>curr+550].index, inplace = True)                  #drop data not within 500 points of the underlying value
data1.drop(data1[data1['strikePrice']<curr-550].index, inplace = True) 

