from database import db

class Food(db.Model):

    __tablename___ = "foods"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    nutritional_value = db.Column(db.String(200))
    unit = db.Column(db.String(20))
    in_stock = db.Column(db.Boolean, default=False)