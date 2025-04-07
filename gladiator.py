import argparse
import json
import numpy as np

# Define global variables defining the calories per gram of each macro.
CALORIES_PER_PROTEIN = 4.0
CALORIES_PER_FAT = 9.0
CALORIES_PER_CARB = 4.0


# Calculate the calories of an ingredient given a serving amount.
def calculate_ingredient_calories(ingredient: dict, serving: float):
    calories = serving * (
        (ingredient["protein"]*CALORIES_PER_PROTEIN)
        + (ingredient["fat"]*CALORIES_PER_FAT)
        + (ingredient["carbs"]*CALORIES_PER_CARB)
    )
    return calories


# Calculate the macros of an ingredient given a serving amount.
def calculate_ingredient_macros(ingredient: dict, serving: float):
    macros = serving * np.array([
        ingredient["protein"],
        ingredient["fat"],
        ingredient["carbs"]
    ])
    return macros


# Calculate the macro distribution of an ingredient given a serving amount.
def calculate_macro_distribution(calories: float, macros: np.ndarray):
    macro_distribution = 100 * np.array([
        (macros[0]*CALORIES_PER_PROTEIN),
        (macros[1]*CALORIES_PER_FAT),
        (macros[2]*CALORIES_PER_CARB)
    ]) / calories
    return macro_distribution


# Converts a list of ingredients into macros and servings.
def ingredients_to_data(ingredients: list[str], amounts: list[float]):
    # TODO: Remove after implementing a proper database.
    with open("ingredients.json", "r") as handle:
        ingredient_database = json.load(handle)

    # Store each ingredient's macros and serving amount.
    nutrition_data = []
    for ingredient, amount in zip(ingredients, amounts):
        ingredient_macros = ingredient_database[ingredient]
        ingredient_serving = amount / ingredient_macros["serving_size"]
        nutrition_data.append((
            ingredient_macros,
            ingredient_serving
        ))

    return nutrition_data


# Converts a list of meals into macros and servings.
def meals_to_data(meals: list[str], amounts: list[float]):
    # TODO: Remove after implementing a proper database.
    with open("meals.json", "r") as handle:
        meal_database = json.load(handle)

    # TODO: Remove after implementing a proper database.
    with open("ingredients.json", "r") as handle:
        ingredient_database = json.load(handle)

    nutrition_data = []
    for meal, amount in zip(meals, amounts):
        # Import the meal's ingredients and serving size from the database.
        meal_data = meal_database[meal]
        meal_ingredients = meal_data["ingredients"]
        meal_serving = amount / meal_data["serving_size"]

        # Store each ingredient's macros and serving amount.
        for ingredient, amount in meal_ingredients.items():
            ingredient_macros = ingredient_database[ingredient]
            ingredient_serving = amount \
                / ingredient_macros["serving_size"] \
                * meal_serving
            nutrition_data.append((ingredient_macros, ingredient_serving))

    return nutrition_data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A convenient way to track your macros."
    )

    parser.add_argument(
        "-m",
        "--mode",
        dest="mode",
        type=str,
        choices=["ingredients", "meals"],
        required=True,
        help="the food abstraction to calculate over"
    )
    parser.add_argument(
        "-f",
        "--foods",
        dest="foods",
        type=str,
        nargs="*",
        required=False,
        help="list of foods"
    )
    parser.add_argument(
        "-a",
        "--amounts",
        dest="amounts",
        type=float,
        nargs="*",
        required=True,
        help="list of food amounts (in grams)"
    )
    parser.add_argument(
        "-q",
        "--quiet",
        dest="quiet",
        action="store_true",
        help="suppress output"
    )
    parser.add_argument(
        "-s",
        "--save",
        dest="save",
        action="store_true",
        help="save results in a csv file"
    )
    parser.add_argument(
        "-u",
        "--user",
        dest="user",
        type=str,
        required=True,
        help="the user to save the results under"
    )
    args = parser.parse_args()

    # Require the user to input a list of ingredients or meals.
    if not args.foods:
        raise Exception("You must input a list of ingredients or meals.")

    # Require the user to input the same number of foods and amounts.
    if len(args.foods) != len(args.amounts):
        raise Exception(
            "The number of foods must match the number of amounts."
        )

    # Initialize our quantities of interest.
    calories = 0
    macros = np.zeros(3, dtype=float)
    distribution = np.zeros(3, dtype=float)

    # Retrieve the nutrition data for the list of foods.
    if args.mode == "meals":
        # Convert the meal list into a list of ingredient macros and servings.
        nutrition_data = meals_to_data(args.foods, args.amounts)
    else:
        # Convert the ingredient list into a list of ingredient macros and
        # servings.
        nutrition_data = ingredients_to_data(args.foods, args.amounts)

    # Compute our quantities of interest for our ingredients.
    for ingredient, serving in nutrition_data:
        calories += calculate_ingredient_calories(ingredient, serving)
        macros += calculate_ingredient_macros(ingredient, serving)
    distribution = calculate_macro_distribution(calories, macros)

    if not args.quiet:
        print(
            f"Total calories: {calories}\n"
            f"Protein: {macros[0]}g Fat: {macros[1]}g Carbs: {macros[2]}g\n"
            f"Protein: {distribution[0]}% Fat: {distribution[1]}% "
            f"Carbs: {distribution[2]}%\n"
        )

    # TODO: Add the date as either part of the filename or as a new column.
    if args.save:
        import csv
        with open(f"data/{args.user}.csv", "a") as handle:
            writer = csv.writer(handle)
            for food, amount in zip(args.foods, args.amounts):
                writer.writerow([
                    food,
                    amount,
                    calories,
                    macros[0],
                    macros[1],
                    macros[2],
                    distribution[0],
                    distribution[1],
                    distribution[2]
                ])
