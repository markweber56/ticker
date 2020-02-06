from flask import render_template, request, session, redirect, url_for
from flask import current_app as app
from .. import db
from ..models import companies, prices
from . import ticker
from .forms import stockForm

print('CHHHHECK   !!!!!! : ',companies)

@ticker.route('/',methods=['GET','POST'])
def index():
    print('you have reached the home base')
    return render_template('alternate.html')

@ticker.route('/buttons',methods=['GET','POST'])
def buttons():
    sesh = db.session

#    companyInfo = sesh.query(companies.tick).all()
    companyInfo = companies.query.all()
    print('company info type: ',type(companyInfo))
    testVal = companyInfo[0]
    print('test value: ',testVal)
    print(testVal.__dict__)
    print('test tick: ',testVal.tick)
    '''
    for c in companyInfo:
        print(c)
    companyNames = companyInfo[0].name

    company = companyInfo.name[0][0]
    id = companyInfo.id[0][0]
    for c in companyNames:
        print(c)
    print('companyNames datatype: ',type(companyNames[0][0]))
    print('company id: ',id)
    '''

    return render_template('buttons.html')

@ticker.route('/plotter',methods=['GET','POST'])
def plotter():

    form = stockForm() # imported from forms.py

    plotData = [] # initialize values to pass to html
    companySelection = ''

    if request.method == 'POST':
        print('!!!!!!!!!!!! A POST HAS BEEN REQUETED !!!!!!')
        companySelection = form.stock_selection.data # company selected by user
        # query db
        q = companies.query.filter_by(name=companySelection).first()
        id = q.id
        print("company ID: ",id)
        data = prices.query.filter_by(company=id).all()
        print("data: ",data[0])
        plotData = []
        print("data dict: ",data[0].__dict__)
        for row in data:
            price = float(row.price)
            dt = str(row.timestamp)
            plotData.append([price,dt])
        print("plotData: ",plotData)

    else:
        print('something other than a POST')



    companyNames = []
    companyInfo = companies.query.all()
    for row in companyInfo:
        name = row.name
    #    print('company name: ',name)
        companyNames.append((name,name))

    form.stock_selection.choices = companyNames
    # print('company names: ',companyNames)

    return render_template('plotter.html',data=plotData,company=companySelection,form=form)

    '''
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
