from database import db

class MenuRecipe(db.Model):
    
    __tablename__ = "menu_recipe"

    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey("menu.id"), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable=False)
    day_part = db.Column(db.String(50), nullable=False)

    menu = db.relationship("Menu", back_populates="recipes")
    recipe = db.relationship("Recipe")
