import csv
import json

dict = {}

with open('NYSE.txt', newline='') as csvfile:
    d = csv.reader(csvfile, delimiter=' ', quotechar='|')
    count = -1
    for row in d:
        count+=1
        if count>0:
            v = row[0].split('\t')
            ticker = v[0]
            print('ticker: ',ticker)
            company = v[1]
            if len(company)>1:
                for i in range(2,len(v)):
                    company+=" "+v[i]
            print('company: ',company)
            dict[company] = {}
            dict[company]["tick"] = ticker
            dict[company]["idx"] = count

            '''
            if count>5:
                break
            '''
print(dict)

with open('NYSE.json', 'w') as fp:
    json.dump(dict, fp)
