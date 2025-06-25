from schemas.recipe_food_schema import recipe_food_schema

def recipe_schema(recipe):
    return {
        "id": recipe.id,
        "name": recipe.name,
        "instructions": recipe.instructions,
        "category": recipe.category,
        "ingredients": [recipe_food_schema(i) for i in recipe.ingredients]
    }

def recipes_schema(recipes):
    return [recipe_schema(recipe) for recipe in recipes]