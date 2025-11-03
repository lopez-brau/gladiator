import json

class Ingredient:
    protein: float
    fat: float
    carbs: float
    serving_size: float

# Adds an ingredient to the database.
def add_ingredients(ingredient: dict):
    # TODO: Remove after implementing a proper database.
    with open("ingredients.json", "r") as handle:
        ingredient_database = json.load(handle)

    # Extract the name of the ingredient we want to add.
    ingredient_name = list(ingredient.keys())[0]

    # Add the ingredient to the database (if it doesn't currently exist).
    with open("ingredients.json", "a") as handle:
        if ingredient_database.get(ingredient_name):
            raise Exception("This ingredient is already in the database.")
        else:
            ingredient_database[ingredient_name] = ingredient[ingredient_name]
            json.dump(ingredient_database, handle, indent=2)


# Adds a meal to the database.
def add_meals():
    # TODO: Remove after implementing a proper database.
    with open("meals.json", "r") as handle:
        meal_database = json.load(handle)


