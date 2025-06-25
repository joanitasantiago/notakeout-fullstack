def food_schema(food):
    return {
        "id": food.id,
        "name": food.name,
        "category": food.category,
        "nutritional_value": food.nutritional_value,
        "unit": food.unit,
        "in_stock": food.in_stock
    }

def foods_schema(foods):
    return [food_schema(food) for food in foods]
