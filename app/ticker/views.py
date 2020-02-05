from flask import render_template, request, session, redirect, url_for
from flask import current_app as app
from .. import db
from ..models import companies
from . import ticker

print('CHHHHECK   !!!!!! : ',companies)

@ticker.route('/',methods=['GET','POST'])
def index():
    print('you have reached the home base mother fucker')
    return render_template('alternate.html')

'''
with open("../text/final_list.json") as jsonFile:
    companyDict = json.load(jsonFile)
'''

@ticker.route('/buttons',methods=['GET','POST'])
def buttons():
    sesh = db.session

    companyNames = sesh.query(companies.name).all()
    for c in companyNames:
        print(c)
    print('companyNames datatype: ',type(companyNames[0][0]))

    return render_template('buttons.html')

'''
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

'''
