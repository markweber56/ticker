import json
import csv

with open("yahooTicks.json") as json_file:
    ticks = json.load(json_file)

companies = list(ticks.keys())

dict = {}
failures = 0

count = 0
with open('shortCompanyList.csv') as csvFile:
    reader = csv.reader(csvFile,delimiter='\t')
    for row in reader:
        company = row[1]
        tick = ticks[company]["tick"]
        dict[company] = {"tick":tick,"idx":count}
        count+=1
        print(tick)

with open("final_list.json","w") as jsonFile:
    json.dump(dict,jsonFile)
