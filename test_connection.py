from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

HOST = 'mwdb1.ciwuxqobkmuk.us-east-2.rds.amazonaws.com'
DB = 'NYSE'
USERNAME = 'markweber56'
PASSWORD = 'AWEjCoYLd1wITLEekE6i'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s' % (USERNAME,PASSWORD,HOST,DB)

engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={'connect_timeout':60})
connection = engine.connect()
