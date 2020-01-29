import requests
import json
from datetime import datetime
import csv

with open("final_list.json") as json_file:
    ticks = json.load(json_file)

companies = list(ticks.keys())

# with open("stockData.csv")
for iteration in range(1000):
    with open('stockData.csv','w') as csvFile:
        writer = csv.writer(csvFile)
        for company in companies:
            try:
                str = 'https://finance.yahoo.com/quote/'+ticks[company]["tick"]
                rsp = requests.get(str)
                #    cnt = rsp.content
                strCnt = rsp.content.decode('unicode_escape')

                stockNum = ticks[company]["idx"]

                sp = strCnt.find("root.App.main")
                str = strCnt[sp:]
                idx = str.find('"regularMarketPrice"')
                #    print('index: ',idx)
                shortStr = str[idx:idx+100].replace('"regularMarketPrice":{"raw":','')
                idx2 = shortStr.find(",")
                priceStr = shortStr[0:idx2]
                dt = datetime.utcnow()
                d = dt.strftime("%Y-%m-0%d %H:%M:%S %f")
                if priceStr=='1.6049999':
                    print('no result')
                else:
                    stockPrice = float(priceStr)
                    outputString = (iteration,stockNum,company,stockPrice,d)

                    print(outputString)
                    writer.writerow(outputString)
            except:
                print(company," failed")
