from flask import Blueprint, request, jsonify
from database import db
from models.food import Food
from schemas.food_schema import food_schema
from schemas.food_schema import foods_schema


food_bp = Blueprint("food_bp", __name__)

@food_bp.route("/foods", methods=["POST"])
def create_food():
    """
    Cadastrar um novo alimento
    ---
    tags:
      - Alimentos
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            category:
              type: string
            nutritional_value:
              type: string
            unit:
              type: string
            in_stock:
              type: boolean
    responses:
      201:
        description: Alimento criado com sucesso
    """
    data = request.get_json()
    new_food = Food(
        name=data.get("name"),
        category=data.get("category"),
        nutritional_value=data.get("nutritional_value"),
        unit=data.get("unit"),
        in_stock=data.get("in_stock", False)
    )
    db.session.add(new_food)
    db.session.commit()

    return jsonify(food_schema(new_food)), 201

@food_bp.route("/foods", methods=["GET"])
def get_all_foods():
    """
    Listar todos os alimentos cadastrados
    ---
    tags:
      - Alimentos
    responses:
      200:
        description: Lista de alimentos retornada com sucesso
    """
    foods = Food.query.all()
    result = foods_schema(foods)
    return jsonify(result), 200

@food_bp.route("/foods/<int:id>", methods=["GET"])
def get_food_by_id(id):
    """
    Buscar um alimento pelo ID
    ---
    tags:
      - Alimentos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do alimento a ser buscado
    responses:
      200:
        description: Alimento encontrado com sucesso
      404:
        description: Alimento não encontrado
    """
    food = Food.query.get(id)

    if not food:
        return jsonify({"message": "Alimento não encontrado"}), 404

    return jsonify(food_schema(food)), 200

@food_bp.route("/foods/<int:id>", methods=["PUT"])
def update_food(id):
    """
    Atualizar um alimento existente
    ---
    tags:
      - Alimentos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do alimento a ser atualizado
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            category:
              type: string
            nutritional_value:
              type: string
            unit:
              type: string
            in_stock:
              type: boolean
    responses:
      200:
        description: Alimento atualizado com sucesso
      404:
        description: Alimento não encontrado
    """
    data = request.get_json()
    food = Food.query.get(id)

    if not food:
        return jsonify({"message": "Alimento não encontrado"}), 404

    food.name = data.get("name", food.name)
    food.category = data.get("category", food.category)
    food.nutritional_value = data.get("nutritional_value", food.nutritional_value)
    food.unit = data.get("unit", food.unit)
    food.in_stock = data.get("in_stock", food.in_stock)

    db.session.commit()

    return jsonify(food_schema(food)), 200


@food_bp.route("/foods/<int:id>", methods=["DELETE"])
def delete_food(id):
    """
    Deletar um alimento pelo ID
    ---
    tags:
      - Alimentos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do alimento a ser deletado
    responses:
      200:
        description: Alimento deletado com sucesso
      404:
        description: Alimento não encontrado
    """
    food = Food.query.get(id)

    if not food:
        return jsonify({"message": "Alimento não encontrado"}), 404

    db.session.delete(food)
    db.session.commit()

    return jsonify({"message": "Alimento deletado com sucesso"}), 200
