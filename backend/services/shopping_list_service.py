def generate_shopping_list(menu):
    items = set()

    for link in menu.recipes: 
        recipe = link.recipe
        for ingredient in recipe.ingredients:
            items.add(ingredient.food.name)

    return sorted(items)  # ordena alfabeticamente
