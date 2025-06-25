def recipe_food_schema(data):
    return {
        "food_id": data.food_id,
        "food_name": data.food.name if data.food else None,
        "quantity": data.quantity,
    }
