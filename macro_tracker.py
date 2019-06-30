import argparse
import numpy as np
import sys

from Food import Food

if __name__ == "__main__":
	food_list = [
		Food(name="egg_noodles", protein=8.0, fat=2.5, carbs=38.0, 
			serving_size=56.0),
		Food(name="quinoa", protein=8.0, fat=2.0, carbs=53.0, 
			serving_size=70.8),
		Food(name="pasta", protein=10.0, fat=2.0, carbs=38.0, 
			serving_size=56.0),
		Food(name="pasta_sauce", protein=2.0, fat=1.5, carbs=12.0, 
			serving_size=120.0),
		Food(name="eggs", protein=6.8, fat=7.4, carbs=1.3, 
			serving_size=1.0),
		Food(name="chicken", protein=9.4, fat=1.3, carbs=0.1, 
			serving_size=28.0),
		Food(name="salmon", protein=24.0, fat=10.0, carbs=0.0, 
			serving_size=85.0),
		Food(name="beef", protein=23.6, fat=7.9, carbs=0.0, 
			serving_size=112.0),
		Food(name="spinach", protein=3.0, fat=0.0, carbs=4.0, 
			serving_size=85.0),
		Food(name="almonds", protein=6.0, fat=14.0, carbs=6.0, 
			serving_size=28.0),
		Food(name="peanut_butter", protein=7.0, fat=16.0, carbs=7.0, 
			serving_size=32.0),
		Food(name="milk", protein=8.0, fat=5.0, carbs=12.0, 
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
			serving_size=32.0)

	]
# 350 chicken 87.5
# 1920 broth 480
# 137 noodles 34.3
	parser = argparse.ArgumentParser(
		description="A convenient way to calculate your total macros."
	)
	   
	parser.add_argument("-f", "--food", dest="food", type=str, nargs="*",
		required=True, help="list of foods")
	parser.add_argument("-s", "--servings", dest="servings", type=float, 
		nargs="*", required=True, help="list of servings")
	args = parser.parse_args()

	if len(args.food) != len(args.servings):
		print("Mismatch between the list of food and list of servings.")
		sys.exit(1)

	calories = 0
	macros = np.array([0, 0, 0])
	for food in food_list:
		for f in range(len(args.food)):
			if food.name == args.food[f]:
				macros = macros + food.calc_macros(args.servings[f])
				calories = calories + food.calc_calories(args.servings[f])

	calories = np.round(calories, decimals=2)
	print(f"Calories: {calories}")
	macros = np.round(macros, decimals=2)
	print(f"Protein: {macros[0]}g, Fats: {macros[1]}g, Carbs: {macros[2]}g")
	distribution = np.round(Food(name="", protein=macros[0], fat=macros[1], \
		carbs=macros[2], serving_size=1).calc_distribution(1), decimals=2)
	print(f"Protein: {distribution[0]}%, Fats: {distribution[1]}%, Carbs: {distribution[2]}%")