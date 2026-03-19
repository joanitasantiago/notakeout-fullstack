import os
from flasgger import Swagger
from flask import Flask
from flask_cors import CORS
from database import db
from routes.food_routes import food_bp
from routes.recipe_routes import recipe_bp
from routes.menu_routes import menu_bp


app = Flask(__name__)
CORS(app)
database_url = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.register_blueprint(food_bp)
app.register_blueprint(recipe_bp)
app.register_blueprint(menu_bp)
swagger = Swagger(app)

@app.route("/")
def home():
    return "API de Gerenciamento de Refeições - MVP"
if __name__ == "__main__":
    app.run(debug=True)
