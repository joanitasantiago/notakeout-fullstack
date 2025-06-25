def menu_recipe_schema(link):
    return {
        "menu_id": link.menu_id,
        "recipe_id": link.recipe_id,
        "recipe_name": link.recipe.name
    }

def menu_recipes_schema(links):
    return [menu_recipe_schema(link) for link in links]