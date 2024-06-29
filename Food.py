class Food:

	def __init__(self, name, protein, fat, carbs, serving_size):
		self.name = name

		# Macros per serving (or per count, if applicable).
		self.protein = protein
		self.fat = fat
		self.carbs = carbs

		# How big each serving is (in grams).
		self.serving_size = serving_size

    # Calculate the calories given an intake amount (in grams).
	def calc_calories(self, intake):
		servings = intake / self.serving_size
		return (self.protein*servings*4.0) \
			+ (self.fat*servings*9.0) \
			+ (self.carbs*servings*4.0)

	def calc_distribution(self, intake):
		servings = intake / self.serving_size
		total_calories = (self.protein*servings*4.0) \
			+ (self.fat*servings*9.0) \
			+ (self.carbs*servings*4.0)
		return [(self.protein*servings*4.0)/total_calories, \
			(self.fat*servings*9.0)/total_calories, \
			(self.carbs*servings*4.0)/total_calories]

	def calc_macros(self, intake):
		servings = intake / self.serving_size
		return [self.protein*servings, self.fat*servings, self.carbs*servings]

# Calc macros per gram
class Meal:

	def __init__(self, name, ingredients):
		self.name = name
		self.ingredients = ingredients

	# def calc_macros(self, intake):
	# 	macros = 0
	# 	for ingredient in self.ingredients:
	# 		macros += ingredient
