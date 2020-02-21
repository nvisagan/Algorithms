#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # If the ingredients dictionary has same as the recipie dictionary
    if recipe.keys() == ingredients.keys():
      batches = []
      for items in recipe:
        #Check if ingredient is larger and then divide 
        if ingredients[items] >= recipe[items]:
          serving = ingredients[items] // recipe[items]
          batches.append(serving)
          #Return min for most number of servings
        return min(batches)
    else:
      #If we don't have enough its zero
      return 0

recipe_batches({ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 198, 'butter': 52, 'cheese': 10})

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))