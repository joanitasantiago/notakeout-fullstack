from flask import Blueprint, request, jsonify
from flask import make_response
from database import db
from models.menu import Menu
from models.menu_recipe import MenuRecipe
from models.recipe import Recipe
from services.shopping_list_service import generate_shopping_list
from services.shopping_list_pdf_service import generate_shopping_list_pdf
from schemas.menu_schema import menu_summary_schema
from schemas.menu_schema import menu_schema
from schemas.menu_schema import menus_schema

menu_bp = Blueprint("menu_bp", __name__)

@menu_bp.route("/menus", methods=["POST"])
def create_menu():
    """
    Cadastrar um novo cardápio
    ---
    tags:
      - Menus
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: Cardápio de Segunda
            recipes:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  day_part:
                    type: string
                    example: almoço
    responses:
      201:
        description: Menu criado com sucesso
      400:
        description: Erro nos dados recebidos
    """
    data = request.get_json()

    title = data.get("title")
    recipe_data = data.get("recipes", [])

    new_menu = Menu(title=title)

    for item in recipe_data:
        recipe_id = item.get("id")
        day_part = item.get("day_part")
        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            continue
    
        link = MenuRecipe(recipe=recipe, day_part=day_part)
        new_menu.recipes.append(link)

    db.session.add(new_menu)
    db.session.commit()

    return jsonify(menu_schema(new_menu)), 201

@menu_bp.route("/menus", methods=["GET"])
def get_all_menus():
    """
    Listar todos os menus cadastrados
    ---
    tags:
      - Menus
    responses:
      200:
        description: Lista de menus retornada com sucesso
    """
    menus = Menu.query.all()
    result = menus_schema(menus)
    return jsonify(result), 200

@menu_bp.route("/menus/<int:id>", methods=["GET"])
def get_menu_by_id(id):
    """
    Buscar um menu pelo ID
    ---
    tags:
      - Menus
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do menu a ser buscado
    responses:
      200:
        description: Menu encontrado com sucesso
      404:
        description: Menu não encontrado
    """
    menu = Menu.query.get(id)

    if not menu:
        return jsonify({"message": "Menu não encontrado"}), 404

    return jsonify(menu_schema(menu)), 200

@menu_bp.route("/menus/<int:id>", methods=["DELETE"])
def delete_menu(id):
    """
    Deletar um menu pelo ID
    ---
    tags:
      - Menus
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do menu a ser deletado
    responses:
      200:
        description: Menu deletado com sucesso
      404:
        description: Menu não encontrado
    """
    menu = Menu.query.get(id)

    if not menu:
        return jsonify({"message": "Menu não encontrado"}), 404

    db.session.delete(menu)
    db.session.commit()

    return jsonify({"message": "Menu deletado com sucesso"}), 200

@menu_bp.route("/menus/<int:id>", methods=["PUT"])
def update_menu(id):
    """
    Atualizar um menu existente
    ---
    tags:
      - Menus
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do menu a ser atualizado
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              title:
                type: string
                example: Cardápio de Terça
              recipes:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: integer
                      example: 2
                    day_part:
                      type: string
                      example: almoço
    responses:
      200:
        description: Menu atualizado com sucesso
      404:
        description: Menu não encontrado
    """
    data = request.get_json()
    menu = Menu.query.get(id)

    if not menu:
        return jsonify({"message": "Menu não encontrado"}), 404

    menu.title = data.get("title", menu.title)
    new_recipes = data.get("recipes", [])

    # Limpar receitas antigas
    menu.recipes.clear()

    # Adicionar novas receitas com parte do dia
    for item in new_recipes:
        recipe_id = item.get("id")
        day_part = item.get("day_part")

        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            continue  # ou retornar erro, se preferir

        link = MenuRecipe(recipe=recipe, day_part=day_part)
        menu.recipes.append(link)

    db.session.commit()

    return jsonify(menu_schema(menu)), 200

@menu_bp.route("/shopping-list/<int:menu_id>", methods=["GET"])
def get_shopping_list(menu_id):
    """
    Gerar lista de compras com base em um menu
    ---
    tags:
      - Menus
    parameters:
      - name: menu_id
        in: path
        type: integer
        required: true
        description: ID do menu para gerar a lista
    responses:
      200:
        description: Lista de compras gerada com sucesso
      404:
        description: Menu não encontrado
    """
    menu = Menu.query.get(menu_id)
    if not menu:
        return jsonify({"message": "Menu não encontrado"}), 404

    items = generate_shopping_list(menu)

    return jsonify({
        "menu_id": menu.id,
        "title": menu.title,
        "items": items
    }), 200

@menu_bp.route("/menus/<int:menu_id>/pdf", methods=["GET"])
def get_shopping_list_pdf(menu_id):
    """
    Gerar PDF da lista de compras de um menu
    ---
    tags:
      - Menus
    parameters:
      - name: menu_id
        in: path
        type: integer
        required: true
        description: ID do menu para gerar o PDF da lista de compras
    responses:
      200:
        description: PDF gerado com sucesso
        content:
          application/pdf:
            schema:
              type: string
              format: binary
      404:
        description: Menu não encontrado
    """
    menu = Menu.query.get(menu_id)
    if not menu:
        return jsonify({"message": "Menu não encontrado"}), 404

    items = generate_shopping_list(menu)

    pdf_data  = generate_shopping_list_pdf(menu, items)

    response = make_response(pdf_data)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = f"attachment; filename=lista_compras_menu_{menu.id}.pdf"

    return response