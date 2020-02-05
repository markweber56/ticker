import os
import json

basedir = os.path.abspath(os.path.dirname(__file__))

# print("directory: ",dir(__file__))
# print("directory number2 !!!: ",dir(basedir))

# with open("../admin/config.json") as jsonFile:
with open("admin/config.json") as jsonFile:
    config = json.load(jsonFile)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'crazyhardtoguessstring'

    @staticmethod
    def init_app(app):
        pass

class RemoteDB(Config):
    DEVELOPMENT = True
    DEBUG = True

    HOST = config["HOST"]
    DB = config["DB"]
    USERNAME = config["USERNAME"]
    PASSWORD = config["PASSWORD"]
    SQLALCHEMY_DATABSE_URI = 'mysql+pymysql://%s:%s@%s/%s' % (USERNAME,PASSWORD,HOST,DB)

class LocalDB(Config):
    DEVELOPMENT = True
    DEBUG = True

    SQLALCHEMY_DATABSE_URI = "sqlite:////home/mark/projects/stocks/db/stock_data.db"

config = {
    'local':LocalDB,
    'remote':RemoteDB
}
