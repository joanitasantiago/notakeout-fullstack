from database import db

# Referência p/ estudo:
# Uma receita pode ter vários alimentos
# Um alimento pode estar em várias receitas
# Relacionamento muitos-para-muitos
# Criar a tabela recipe_food para intermediar a ligação entre alimentos e receitas
# No SQLAlchemy, para relacionamentos many-to-many, a tabela intermediária é obrigatória

class RecipeFood(db.Model):

    __tablename__ = "recipe_food"

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey("food.id"), nullable=False)
    quantity = db.Column(db.String(100), nullable=False)

    # relations
    recipe = db.relationship("Recipe", back_populates="ingredients")
    food = db.relationship("Food")