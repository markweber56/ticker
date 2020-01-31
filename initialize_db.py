from sqlalchemy import (create_engine, MetaData, Table, Integer, String,
    ForeignKey, DateTime,   PrimaryKeyConstraint, UniqueConstraint,
    CheckConstraint, Column, Numeric, insert)
import json
import os

with open("admin/config.json") as jsonFile:
    config = json.load(jsonFile)

with open("text/final_list.json") as jsonFile:
    companyDict = json.load(jsonFile)

keys = list(companyDict.keys())

print(companyDict[keys[0]].keys())

HOST = config["HOST"]
DB = config["DB"]
USERNAME = config["USERNAME"]
PASSWORD = config["PASSWORD"]

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s' % (USERNAME,PASSWORD,HOST,DB)

engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={'connect_timeout':60})
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

for company in keys:
    ins = companies.insert().values(
        name = company,
        tick = companyDict[company]["tick"]
    )
    result = connection.execute(ins)
