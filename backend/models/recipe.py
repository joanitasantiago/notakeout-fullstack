from database import db
from models.recipe_food import RecipeFood

class Recipe(db.Model):

    __tablename__ = "recipe"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)

    # aqui faz a conexão com recipe_food
    ingredients = db.relationship("RecipeFood", back_populates="recipe", cascade="all, delete-orphan") # se apagar a receita, os ingredientes também são apagados automaticamente (evita lixo no banco)
