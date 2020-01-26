import requests
import json
from utilities import between

tickers = {"amazon":"AMZN",
            "american express company":"AXP",
            "apple":"APPL",
            "united states steel corporation":"X"}
stock = "american express company"
rsp = requests.get('https://finance.google.com/finance?q='+tickers[stock]+'&output=json')
# print('Response type: ',type(rsp))
cnt = rsp.content
# print('Content type: ',type(cnt))
strCnt = rsp.content.decode('unicode_escape')
print('Decoded type: ',type(strCnt))

text_file = open('str.txt','w')
text_file.write(strCnt)
text_file.close()

'''
strList = strCnt.split('>')
with open('strList.html','w') as file:
    for s in strList:
        file.write(s+'>\n')
'''

idx = strCnt.find("Stock Price")
# print('index: ',idx)
short = strCnt[idx:idx+500]
# print(short)

# print("short: ",short)

arr = between(short,">","<")
print("between: ", arr)
