import requests
import json
from datetime import datetime
import csv
import os
from flask_sqlalchemy import SQLAlchemy
# from SQLAlchemy import create_engine

# path = 'text','final_list.json')

with open('text/final_list.json') as json_file:
    ticks = json.load(json_file)

companies = list(ticks.keys())

# with open("stockData.csv")
# path = os.path.join(os.path.expanduser('~'),'projects','stocks','text','stockData.csv')
with open('text/stockData2.csv','w') as csvFile:
    writer = csv.writer(csvFile)
    for iteration in range(1):
        for company in companies:
            try:
                str = 'https://finance.yahoo.com/quote/'+ticks[company]["tick"]
                time0 = datetime.now()
                rsp = requests.get(str, timeout=3)
                time1 = datetime.now()
                rspTime = (time1-time0).total_seconds()

                #    cnt = rsp.content
                strCnt = rsp.content.decode('unicode_escape')

                stockNum = ticks[company]["idx"]

                time0 = datetime.now()
                sp = strCnt.find("root.App.main")
                str = strCnt[sp:]
                idx = str.find('"regularMarketPrice"')
                #    print('index: ',idx)
                shortStr = str[idx:idx+100].replace('"regularMarketPrice":{"raw":','')
                idx2 = shortStr.find(",")
                priceStr = shortStr[0:idx2]
                time1 = datetime.now()
                parseTime = (time1-time0).total_seconds()

                dt = datetime.utcnow()
                d = dt.strftime("%Y-%m-0%d %H:%M:%S %f")
                if priceStr=='1.6049999':
                    print('no result')
                else:
                    stockPrice = float(priceStr)
                    outputString = (iteration,stockNum,company,stockPrice,d)

                    print(outputString)
                    print("request time: ",rspTime,' parseTime: ',parseTime)
#                    writer.writerow(outputString)
            except:
                print(company," failed")
