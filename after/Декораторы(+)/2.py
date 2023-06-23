def add_ingredients(recipe_func):
    def wrapper():
        return recipe_func() + ", Салат, Ананасы"
    return wrapper

@add_ingredients
def sandwich_recipe():
    return "Хлеб, Масло, Ветчина, Сыр"

decorated_recipe = sandwich_recipe()
print(decorated_recipe)
