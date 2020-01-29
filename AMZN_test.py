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
# str = 'https://finance.google.com/finance?q=A&output=json'
str = 'https://www.google.com/search?q=AMZN&tbm=fin'
rsp = requests.get(str)
# print('Response type: ',type(rsp))
cnt = rsp.content
# print('Content type: ',type(cnt))
strCnt = rsp.content.decode('unicode_escape')

# write text file
strList = strCnt.split('>')
with open('strList.html','w') as file:
    for s in strList:
        file.write(s+'>\n')

idx = strCnt.find("Stock Price")
print('index: ',idx)
short = strCnt[idx:idx+500]

arr = between(short,">","<")
priceStr = arr[0].replace(',','')
price = float(priceStr)
print("Amazon"," close: $",price)
