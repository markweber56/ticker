from . import db

class companies(db.Model):

    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), unique=True)
    tick = db.Column(db.String(10), unique=True)

    def __repr__(self):
        return '<Company: %r>' % self.name
