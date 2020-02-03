from flask import Flask, render_template, session
from flask_bootstrap import Bootstrap
from sqlalchemy import (create_engine, MetaData, Table, String, ForeignKey,
    DateTime, Column, Numeric, Integer)
from sqlalchemy.sql import select
import json
from datetime import datetime

app = Flask(__name__)

with open("../text/final_list.json") as jsonFile:
    companyDict = json.load(jsonFile)

@app.route('/',methods=['GET','POST'])
def index():
    # return render_template('home_base.html')

    return render_template('alternate.html')

@app.route('/buttons',methods=['GET','POST'])
def buttons():
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

    s = select([companies]).where(companies.c.name==keys[2])
    rp = connection.execute(s)
    results = rp.fetchall()
    id = results[0][0]
    s = select([prices]).where(prices.c.company==id)
    rp = connection.execute(s)
    result = rp.fetchall()
    '''
    for row in data:
        print('price: ',data[2],'timestamp: ',data[3])
    '''
    test = result[0]
    print('type: ',type(test))
    print(test)
    price = test.price
    print("price: ",price)
    d = []
    dt = test.timestamp
    for r in result:
        price = float(r.price)
        dt = str(r.timestamp)

        d.append([price,dt])

    print(s)
    print("type: ",type(d))

    return render_template('plotter.html',data=d)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
