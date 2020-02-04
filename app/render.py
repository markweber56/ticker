from flask import Flask, render_template, session
from flask_bootstrap import Bootstrap
from sqlalchemy import (create_engine, MetaData, Table, String, ForeignKey,
    DateTime, Column, Numeric, Integer)
from sqlalchemy.sql import select
import json
from datetime import datetime
from forms import stockForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a hard to guess string'

with open("../text/final_list.json") as jsonFile:
    companyDict = json.load(jsonFile)

@app.route('/',methods=['GET','POST'])
def index():
    # return render_template('home_base.html')

    return render_template('alternate.html')

@app.route('/buttons',methods=['GET','POST'])
def buttons():
    return render_template('buttons.html')

@app.route('/plotter',methods=['GET','POST'])
def plotter():
    # get company names from list of 50
    keys = list(companyDict.keys())

    form = stockForm() # imported from forms.py

    # connect to either local or remote db
    dbType = "AWS"
    if dbType == "AWS":
        with open("../admin/config.json") as jsonFile:
            config = json.load(jsonFile)

        HOST = config["HOST"]
        DB = config["DB"]
        USERNAME = config["USERNAME"]
        PASSWORD = config["PASSWORD"]
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s' % (USERNAME,PASSWORD,HOST,DB)
        engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={'connect_timeout':60})
        print("connected to AWS")
    elif dbType == "local":
        engine = create_engine("sqlite:////home/mark/projects/stocks/db/stock_data.db")

    connection = engine.connect() # establish connection
    metadata = MetaData()

    # db table definitions
    companies = Table('companies',metadata,
                    Column('id',Integer(),primary_key=True),
                    Column('name',String(50),unique=True),
                    Column('tick',String(10),unique=True))

    prices = Table('prices',metadata,
                Column('id',Integer(),primary_key=True),
                Column('company',ForeignKey('companies.id')),
                Column('price',Numeric(10,4)),
                Column('timestamp',DateTime()))

    # select data based on company, will be from form
    companyName = keys[40]
    s = select([companies]).where(companies.c.name==companyName)

    rp = connection.execute(s) # get company id key from company name
    results = rp.fetchall()
    id = results[0][0]
    s = select([prices]).where(prices.c.company==id) # select price data
    rp = connection.execute(s)
    result = rp.fetchall()

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

    return render_template('plotter.html',data=d,company=companyName)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
