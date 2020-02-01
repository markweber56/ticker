from sqlalchemy import (create_engine, MetaData, Table, Integer, String, ForeignKey, DateTime,
    PrimaryKeyConstraint, UniqueConstraint, CheckConstraint, Column, Numeric)
from sqlalchemy.dialects.postgresql import JSON
import json
import os

with open("admin/config.json") as jsonFile:
    config = json.load(jsonFile)

HOST = config["HOST"]
DB = config["DB"]
USERNAME = config["USERNAME"]
PASSWORD = config["PASSWORD"]

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s' % (USERNAME,PASSWORD,HOST,DB)

# engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={'connect_timeout':60})
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

metadata.create_all(engine)
print("success!")
