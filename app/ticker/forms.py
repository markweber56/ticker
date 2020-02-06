from flask_wtf import FlaskForm
from wtforms import SelectField

class stockForm(FlaskForm):

    '''
    form form for selecting stock from strList
    '''
    stock_selection = SelectField('Company: ',choices=[])
