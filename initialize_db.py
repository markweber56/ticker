from sqlalchemy import (create_engine, MetaData, Table, Integer, String,
    ForeignKey, DateTime,   PrimaryKeyConstraint, UniqueConstraint,
    CheckConstraint, Column, Numeric, insert, select)
import json
import os
import csv
from datetime import datetime

dbType = "AWS" #option2 = "local"

with open("text/final_list.json") as jsonFile: # load ticker info
    companyDict = json.load(jsonFile)

keys = list(companyDict.keys())

print(companyDict[keys[0]].keys())

if dbType=="AWS":
    with open("admin/config.json") as jsonFile:
        config = json.load(jsonFile)

    HOST = config["HOST"]
    DB = config["DB"]
    USERNAME = config["USERNAME"]
    PASSWORD = config["PASSWORD"]
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s' % (USERNAME,PASSWORD,HOST,DB)
    engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={'connect_timeout':60})
elif dbType=="local":
    engine = create_engine("sqlite:////home/mark/projects/stocks/db/stock_data.db")

connection = engine.connect()
metadata = MetaData()

companies = Table('companies',metadata,
                Column('id',Integer(),primary_key=True),
                Column('name',String(50),unique=True),
                Column('tick',String(10),unique=True))

prices = Table('prices',metadata,
            Column('id',Integer(),primary_key=True),
            Column('company',ForeignKey('companies.id')),
            Column('price',Numeric(10,4)),
            Column('timestamp',DateTime()))
''' add company
for company in keys:
    ins = companies.insert().values(
        name = company,
        tick = companyDict[company]["tick"]
    )
    result = connection.execute(ins)
'''
fmt = '%Y-%m-%d %H:%M:%S %f'
# timeVal = datetime.strptime(dateStr, fmt)

'%Y-%m-%d %H:%M:%S %f'
rowNum = 0
with open("text/stockData.csv") as csvFile: # load recorded stock prices
    reader = csv.reader(csvFile,delimiter=',')
    for row in reader:
        print("row#: ",rowNum)
        rowNum+=1
        company = row[2]
        # s = select([companies]).where(companies.name == company)
        s = select([companies.c.id]).where(companies.c.name==company) # get foreign key
        rp = connection.execute(s)
        results = rp.fetchall()

        dateStr = row[4]
        strList = list(dateStr)
        strList[8]='' # remove padded 0
        dateStr = ''
        for c in strList:
            dateStr+=c

        dt = datetime.strptime(dateStr, fmt)

        ins = prices.insert().values(
            company = results[0][0],
            price = row[3],
            timestamp = dt
        )
        result = connection.execute(ins)
