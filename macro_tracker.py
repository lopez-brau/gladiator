import argparse
import json
import numpy as np
import sys

from Food import Food

"""
TO-DO:
- Implement a storage solution to store:
    - Delete function.
    - Alphabetize automatically.
- Implement a `serving_unit` argument to convert between ounces and grams.
"""


# Update the foods in the database.
# TODO: Work on adding foods through CLI.
def add_foods(food):
    """
    food (dict):
        name (str)
        protein (float)
        fat (float)
        carbs (float)
        serving_size (float)
    """
    # Read the current list of foods.
    foods = import_foods()

    # Manipulate food list.
    with open("foods.json", "w") as handler:
        # Ensure the food doesn't currently exist in the database.
        if foods.get(list(food.keys())[0]):
            print("This item is already in the database.")
            return 1
        else:
            foods[list(food.keys())[0]] = food[list(food.keys())[0]]
            json.dump(foods, handler, indent=2)

def import_foods():
    with open("foods.json", "r") as handler:
        foods = json.load(handler)
    return foods

def add_meals():
    pass

if __name__ == "__main__":
    food_list = [
        Food(name="penne_pasta", protein=10.0, fat=2.0, carbs=38.0,
            serving_size=56.0),
        Food(name="pasta_sauce", protein=2.0, fat=1.5, carbs=12.0,
            serving_size=120.0),
        Food(name="eggs", protein=6.8, fat=7.4, carbs=1.3,
            serving_size=1.0),
        Food(name="chicken", protein=9.4, fat=1.3, carbs=0.1,
            serving_size=28.0),
        Food(name="salmon", protein=24.0, fat=10.0, carbs=0.0,
            serving_size=85.0),
        Food(name="beef_93-7", protein=23.6, fat=7.9, carbs=0.0,
            serving_size=112.0),
        Food(name="spinach", protein=3.0, fat=0.0, carbs=4.0,
            serving_size=85.0),
        Food(name="almonds", protein=6.0, fat=14.0, carbs=6.0,
            serving_size=28.0),
        Food(name="peanut_butter", protein=7.0, fat=16.0, carbs=7.0,
            serving_size=32.0),
        Food(name="milk", protein=13.0, fat=4.5, carbs=6.0,
            serving_size=240.0),
        Food(name="orange_juice", protein=2.0, fat=0.0, carbs=26.0,
            serving_size=240.0),
        Food(name="chicken_broth", protein=1.0, fat=0.0, carbs=0.0,
            serving_size=240.0),
        Food(name="protein_powder", protein=32.0, fat=3.0, carbs=8.0,
            serving_size=52.0),
        Food(name="bananas", protein=1.5, fat=0.4, carbs=31.1,
            serving_size=1.0),
        Food(name="strawberries", protein=0.6, fat=0.0, carbs=13.0,
            serving_size=140.0),
        Food(name="honey", protein=0.0, fat=0.0, carbs=17.0,
            serving_size=32.0),
        Food(name="white_rice", protein=3.5, fat=0.3, carbs=36.7,
            serving_size=174.0),
        Food(name="cavatappi_pasta", protein=10.0, fat=1.0, carbs=38.0,
            serving_size=56.0),
        Food(name="beef_90-10", protein=22.0, fat=11.0, carbs=0.0,
            serving_size=112.0),
        Food(name="cheese_mixed-blend", protein=7.0, fat=9.0, carbs=1.0,
            serving_size=28.0),
        Food(name="sour_cream", protein=1.0, fat=5.0, carbs=2.0,
            serving_size=30.0),
        Food(name="poblano_peppers", protein=0.6, fat=0.1, carbs=3.0,
            serving_size=64),
        Food(name="tomatoes_diced", protein=1.0, fat=0.0, carbs=5.0,
            serving_size=121.0),
        Food(name="butter", protein=0.0, fat=11.0, carbs=0.0,
            serving_size=14.1), #3tbsp
        Food(name="olive_oil", protein=0.0, fat=14.0, carbs=0.0,
            serving_size=14.1) #2tbsp
    ]
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
    # meal_list = [
    #   Meal(
    #       name = "Southwest Beef Cavatappi",
    #       ingredients = [
    #           { "name": "poblano_pepper" , "amount": 192.0},
    #           { "name": "cavatappi_pasta" , "amount": 510.0},
    #           { "name": "90/10_beef" , "amount": 1034.0},
    #           { "name": "tomato", "amount": 595.0},
    #           { "name": "sour_cream" , "amount": 90.0},
    #           { "name": "cheese" , "amount": 84.0}
    #       ]
    #   )
    # ]


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
