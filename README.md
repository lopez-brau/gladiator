# Gladiator

`gladiator` computes (and stores) the total calories and macro distribution of a given meal or list of ingredients.

## Usage

```sh
python macro_tracker.py -f cavatappi_pasta beef_90-10 sour_cream cheese_mixed-blend poblano_peppers tomato butter olive_oil -a 510 1034 90 84 192 595 42.3 28.2
```

Calories: 4184.96
Protein: 323.1g, Fats: 152.66g, Carbs: 379.66g
Protein: 31.0%, Fats: 33.0%, Carbs: 36.0%

## To-do

The goal of this app is to:
1. Choose a mode (meal vs. ingredient calc)
2. Input meal or ingredients, along with amount (in grams)
3. Get out total calories and macro distribution

Ingredients/meals are currently being stored and retrieved from json files. Should work on additional functions to add/remove/edit these entries, with the eventual goal of moving them to an actual database platform.
