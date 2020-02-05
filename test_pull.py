from sqlalchemy import (create_engine, MetaData, Table, Integer, String,
    ForeignKey, DateTime, PrimaryKeyConstraint, UniqueConstraint,
    CheckConstraint, Column, Numeric, insert)
from sqlalchemy.sql import select
import json
import os

with open("text/final_list.json") as jsonFile:
    companyDict = json.load(jsonFile)

keys = list(companyDict.keys())

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
'''
s = select([companies])
rp = connection.execute(s)
results = rp.fetchall()
'''

s = select([companies]).where(companies.c.name==keys[2])


rp = connection.execute(s)
results = rp.fetchall()
# print(results)
id = results[0][0]

s = select([prices]).where(prices.c.company==id)

rp = connection.execute(s)
results = rp.fetchall()
# print(results)
print('Types: ',type(results[0]))
idx = 0


for result in results:
    idx+=1
#    print("idx: ",idx," ",result)
    print('price: ',result[2],'timestamp: ',result[3])
'''
i = 0
for val in results[0]:
#    print("value: ",val)
    print("price: ",results[2],' timestamp: ',results[3])
'''
