from . import db

class companies(db.Model):

    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)

    priceRef = db.relationship('prices', backref='companies')
    name = db.Column(db.String(50), unique=True)
    tick = db.Column(db.String(10), unique=True)

    def __repr__(self):
        return '<Company: %r>' % self.name

class prices(db.Model):

    __tablename__ = "prices"

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.Integer, db.ForeignKey('companies.id'))
    price = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<Company id: %r>' % self.company
