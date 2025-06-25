from database import db
from models.menu_recipe import MenuRecipe

class Menu(db.Model):

    __tablename__ = "menu"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    recipes = db.relationship("MenuRecipe", back_populates="menu", cascade="all, delete-orphan")
