from flask import Blueprint, request, jsonify
from database import db
from models.recipe import Recipe
from models.recipe_food import RecipeFood
from models.food import Food
from schemas.recipe_schema import recipe_schema
from schemas.recipe_schema import recipes_schema
from schemas.recipe_food_schema import recipe_food_schema


recipe_bp = Blueprint("recipe_bp", __name__)

@recipe_bp.route("/recipes", methods=["POST"])
def create_recipe():
    """
    Criar uma nova receita
    ---
    tags:
      - Receitas
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: Panqueca de banana
            instructions:
              type: string
              example: Misture tudo e frite
            category:
              type: string
              example: Café da manhã
            ingredients:
              type: array
              items:
                type: object
                properties:
                  name:
                    type: string
                    example: banana
                  quantity:
                    type: string
                    example: "2 unidades"
    responses:
      201:
        description: Receita criada com sucesso
      400:
        description: Dados inválidos
    """
    data = request.get_json()

    new_recipe = Recipe(
        name=data.get("name").strip(),
        instructions=data.get("instructions").strip(),
        category=data.get("category").strip()
    )

    for item in data.get("ingredients", []):
        food_name = item["name"].strip().lower()
        quantity = item["quantity"].strip()

        existing_food = Food.query.filter(db.func.lower(Food.name) == food_name).first()

        if existing_food:
            food = existing_food
        else:
            food = Food(
                name=item["name"].strip().title(),
                category="Desconhecida",
                nutritional_value="",
                unit="unidade",
                in_stock=True
            )
            db.session.add(food)
            db.session.flush()  # Garante acesso ao food.id

        rf = RecipeFood(
            food_id=food.id,
            quantity=quantity
        )
        new_recipe.ingredients.append(rf)

    db.session.add(new_recipe)
    db.session.commit()

    return jsonify(recipe_schema(new_recipe)), 201

@recipe_bp.route("/recipes", methods=["GET"])
def get_all_recipes():
    """
    Listar todas as receitas cadastrados
    ---
    tags:
      - Receitas
    responses:
      200:
        description: Lista de receitas retornada com sucesso
    """
    recipes = Recipe.query.all()
    result = recipes_schema(recipes)
    return jsonify(result), 200

@recipe_bp.route("/recipes/<int:id>", methods=["GET"])
def get_recipe_by_id(id):
    """
    Buscar uma receita pelo ID
    ---
    tags:
      - Receitas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da receita a ser buscada
    responses:
      200:
        description: Receita encontrada com sucesso
      404:
        description: Receita não encontrada
    """

    recipe = Recipe.query.get(id)

    if not recipe:
        return jsonify({"message": "Receita não encontrada"}), 404
    
    return jsonify(recipe_schema(recipe)), 200

@recipe_bp.route("/recipes/<int:id>", methods=["PUT"])
def update_recipe(id):
    """
Atualizar uma receita existente
---
tags:
  - Receitas
parameters:
  - name: id
    in: path
    type: integer
    required: true
    description: ID da receita a ser atualizada
  - name: body
    in: body
    required: true
    schema:
      type: object
      properties:
        name:
          type: string
          example: omelete
        category:
          type: string
          example: café da manhã
        instructions:
          type: string
          example: bata os ovos e frite
        ingredients:
          type: array
          items:
            type: object
            properties:
              name:
                type: string
                example: ovo
              quantity:
                type: string
                example: 2 unidades
responses:
  200:
    description: Receita atualizada com sucesso
  404:
    description: Receita não encontrada
    """
    data = request.get_json()
    recipe = Recipe.query.get(id)

    if not recipe:
        return jsonify({"message": "Receita não encontrada"}), 404

    # Atualizar campos básicos
    recipe.name = data.get("name")
    recipe.category = data.get("category")
    recipe.instructions = data.get("instructions")

    # Limpar ingredientes antigos
    recipe.ingredients.clear()

    # Adicionar novos ingredientes
    for ingredient_data in data.get("ingredients", []):
        food_name = ingredient_data.get("name", "").strip().lower()
        quantity = ingredient_data.get("quantity", "").strip()

        existing_food = Food.query.filter(db.func.lower(Food.name) == food_name).first()
        if existing_food:
            food = existing_food
        else:
            food = Food(
                name=ingredient_data.get("name", "").strip().title(),
                category="Desconhecida",
                nutritional_value="",
                unit="unidade",
                in_stock=True
            )

            db.session.add(food)
            db.session.flush()  # Garante acesso ao food.id

        rf = RecipeFood(
            food_id=food.id,
            quantity=quantity
        )
        recipe.ingredients.append(rf)

    db.session.commit()

    return jsonify(recipe_schema(recipe)), 200

@recipe_bp.route("/recipes/<int:id>", methods=["DELETE"])
def delete_recipe(id):
    """
    Deletar uma receita pelo ID
    ---
    tags:
      - Receitas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da receita a ser deletada
    responses:
      200:
        description: Receita deletada com sucesso
      404:
        description: Receita não encontrada
    """
    recipe = Recipe.query.get(id)

    if not recipe:
        return jsonify({"error": "Receita não encontrada"}), 404

    db.session.delete(recipe)
    db.session.commit()

    return jsonify({"message": "Receita deletada com sucesso"}), 200