from flask import Blueprint

ticker = Blueprint('ticker',__name__)

from . import views

print('!!!!!!!!!!!!!!! intiate ticker !!!!!!!!!!!!!!!!1')
print(views)
