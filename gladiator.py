import argparse
import json
import numpy as np
import sys

# Define global variables containing the calories per macronutrient gram.
CALORIES_PER_PROTEIN = 4.0
CALORIES_PER_FAT = 9.0
CALORIES_PER_CARB = 4.0


# Calculate the calories of an ingredient given an intake amount.
def calculate_ingredient_calories(ingredient, amount):
    servings = amount / ingredient["serving_size"]
    calories = (ingredient["protein"]*CALORIES_PER_PROTEIN*servings) \
        + (ingredient["fat"]*CALORIES_PER_FAT*servings) \
        + (ingredient["carbs"]*CALORIES_PER_CARB*servings)
    return calories


# Calculate the macros of an ingredient given an intake amount.
def calculate_ingredient_macros(ingredient, amount):
    servings = amount / ingredient["serving_size"]
    macros = [
        ingredient["protein"] * servings,
        ingredient["fat"] * servings,
        ingredient["carbs"] * servings
    ]
    return macros


# Calculate the macro distribution of an ingredient given an intake amount.
def calculate_ingredient_distribution(ingredient, amount):
    calories = calculate_ingredient_calories(ingredient, amount)
    macro_distribution = [
        (ingredient["protein"]*CALORIES_PER_PROTEIN*servings) / calories,
        (ingredient["fat"]*CALORIES_PER_FAT*servings) / calories,
        (ingredient["carbs"]*CALORIES_PER_CARB*servings*4.0) / calories
    ]
    return macro_distribution


# Calculate the macros of a meal.
def calculate_meal_macros(meal, amount):
    for ingredient in meal["ingredients"]:
        pass


def import_ingredients():
    with open("ingredients.json", "r") as handler:
        ingredients = json.load(handler)
    return ingredients

# Update the ingredients in the database.
def add_ingredients(ingredient):
    """
    food (dict):
        name (str)
        protein (float)
        fat (float)
        carbs (float)
        serving_size (float)
    """
    # Read the current list of ingredients.
    ingredients = import_ingredients()

    # Manipulate ingredients list.
    with open("ingredients.json", "w") as handler:
        # Ensure the ingredient doesn't currently exist in the database.
        if ingredients.get(list(ingredient.keys())[0]):
            print("This item is already in the database.")
            return 1
        else:
            ingredients[list(ingredient.keys())[0]] = ingredient[list(ingredient.keys())[0]]
            json.dump(ingredients, handler, indent=2)

def import_meals():
    pass

def add_meals():
    pass

if __name__ == "__main__":
    """
    with open("foods.json", "w") as handler:
        entries = {}
        #entries = []
        for food in food_list:
            entries[food.name] = {
                "protein": food.protein,
                "fat": food.fat,
                "carbs": food.carbs,
                "serving_size": food.serving_size
            }
        json.dump(entries, handler, indent=2)
    sys.exit("Done!")
    """
    ingredients = import_ingredients()
    print(calculate_ingredient_macros(ingredients["butter"], 40.0))
    print(calculate_ingredient_calories(ingredients["butter"], 40.0))
    print(calculate_ingredient_distribution(ingredients["butter"], 40.0))
    sys.exit("Done!")
    parser = argparse.ArgumentParser(
        description="A convenient way to calculate your total macros."
    )

    parser.add_argument("-f", "--food", dest="food", type=str, nargs="*",
        required=True, help="list of foods")
    parser.add_argument("-a", "--amount", dest="amount", type=float,
        nargs="*", required=True, help="list of amount (in grams)")
    args = parser.parse_args()

    if len(args.food) != len(args.amount):
        print("Mismatch between the list of food and list of amounts.")
        sys.exit(1)

    calories = 0
    macros = np.array([0, 0, 0])
    for food in food_list:
        for f in range(len(args.food)):
            if food.name == args.food[f]:
                macros = macros + food.calc_macros(args.amount[f])
                calories = calories + food.calc_calories(args.amount[f])

    calories = np.round(calories, decimals=2)
    print(f"Calories: {calories}")
    macros = np.round(macros, decimals=2)
    print(f"Protein: {macros[0]}g, Fats: {macros[1]}g, Carbs: {macros[2]}g")
    distribution = np.round(Food(name="", protein=macros[0], fat=macros[1], \
        carbs=macros[2], serving_size=1).calc_distribution(1), decimals=2) * 100.0
    print(f"Protein: {distribution[0]}%, Fats: {distribution[1]}%, Carbs: {distribution[2]}%")
    weight = sum(args.amount)
    print(f"Weight: {weight}g")
    print(f"Macros per gram:\nProtein: {macros[0]/weight}, Fats: {macros[1]/weight}%, Carbs: {macros[2]/weight}%")
