from flasgger import Swagger
from flask import Flask
from flask_cors import CORS
from database import db
from routes.food_routes import food_bp
from routes.recipe_routes import recipe_bp
from routes.menu_routes import menu_bp


app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notakeout.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.register_blueprint(food_bp)
app.register_blueprint(recipe_bp)
app.register_blueprint(menu_bp)
swagger = Swagger(app)

# Criação automática do banco ao iniciar o app (Flask >=2.3)
from models.food import Food
from models.recipe_food import RecipeFood
from models.recipe import Recipe
from models.menu import Menu
from models.menu_recipe import MenuRecipe
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "API de Gerenciamento de Refeições - MVP"
if __name__ == "__main__":
    app.run(debug=True)