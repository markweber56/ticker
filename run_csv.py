import csv

with open('text/stockData.csv') as csvFile:
    count = 0
    reader = csv.reader(csvFile, delimiter=',')
    for row in reader:
        print(row)
        count+=1
        if count>10:
            break
