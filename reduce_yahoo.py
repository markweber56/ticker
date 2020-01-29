import requests
import json
from utilities import between

with open("NYSE.json") as json_file:
    ticks = json.load(json_file)

companies = list(ticks.keys())

dict = {}
failures = 0

for i in range(len(companies)):
    company = companies[i]

#company = "Associated"

    str = 'https://finance.yahoo.com/quote/'+ticks[company]["tick"]
    rsp = requests.get(str)
    #    cnt = rsp.content
    strCnt = rsp.content.decode('unicode_escape')

    sp = strCnt.find("root.App.main")
    str = strCnt[sp:]
    idx = str.find('"regularMarketPrice"')
    #    print('index: ',idx)
    shortStr = str[idx:idx+100].replace('"regularMarketPrice":{"raw":','')
    idx2 = shortStr.find(",")
    priceStr = shortStr[0:idx2]
    if priceStr!='1.6049999':
        try:
            stockPrice = float(priceStr)
            print(company,' $',stockPrice)
            dict[company]=ticks[company]
        except:
            failures+=1
    else:
        failures+=1


print("failures: ",failures)
with open("yahooTicks.json","w") as f:
    json.dump(dict,f)
