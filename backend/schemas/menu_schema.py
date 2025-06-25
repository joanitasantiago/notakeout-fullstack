def menu_summary_schema(recipe_link):
    if not recipe_link.recipe:
        return None
    return {
        "id": recipe_link.recipe.id,
        "name": recipe_link.recipe.name,
        "ingredients": [link.food.name for link in recipe_link.recipe.ingredients],
        "day_part": recipe_link.day_part
    }

def menu_schema(menu):
    return {
        "id": menu.id,
        "title": menu.title,
        "recipes": [summary for summary in (menu_summary_schema(link) for link in menu.recipes) if summary]
    }

def menus_schema(menus):
    return [menu_schema(menu) for menu in menus]