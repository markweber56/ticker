import requests
import json
from utilities import between

with open("NYSE.json") as json_file:
    ticks = json.load(json_file)

# print("json: ",ticks)

companies = list(ticks.keys())
'''
for c in companies:
    print(c)
'''

for i in range(200):
# for stock in companies:
    stock = companies[i]
    print("tick: ",ticks[stock]["tick"])

    try:
        str = 'https://finance.google.com/finance?q='+ticks[stock]["tick"]+'&output=json'
        print(str)
        rsp = requests.get(str)
        # print('Response type: ',type(rsp))
        cnt = rsp.content
        # print('Content type: ',type(cnt))
        strCnt = rsp.content.decode('unicode_escape')

        idx = strCnt.find("Stock Price")
        print('index: ',idx)
        short = strCnt[idx:idx+500]

        arr = between(short,">","<")
        price = float(arr[0])
        print(stock," close: $",price)
    except:
        x=0
