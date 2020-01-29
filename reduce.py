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

dict = {}
for i in range(70:len(companies)):

    stock = companies[i]
    print("tick: ",ticks[stock]["tick"]," #",i)

    try:
        str = 'https://finance.google.com/finance?q='+ticks[stock]["tick"]+'&output=json'
        rsp = requests.get(str)
        strCnt = rsp.content.decode('unicode_escape')

        idx = strCnt.find("Stock Price")
        # print('index: ',idx)
        short = strCnt[idx:idx+500]

        arr = between(short,">","<")
        price = float(arr[0])
        dict[stock] = ticks[stock]
        print(stock," close: $",price)
    except:
        x=0

print(dict)
with open("tickers.json") as f:
    json.dump(dict,f)
