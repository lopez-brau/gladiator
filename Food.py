class Food:
	
	def __init__(self, name, protein, fat, carbs, serving_size):
		self.name = name

		# Macros per serving (per count if applicable).
		self.protein = protein
		self.fat = fat
		self.carbs = carbs

		# How big each serving is (in grams).
		self.serving_size = serving_size

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

# class Meal:

# 	def __init__(self, name, foods):
#		self.name = name
# 		self.foods = foods

# 	def calc_macros(self, intake):
# 		