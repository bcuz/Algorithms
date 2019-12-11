#!/usr/bin/python

import math
# n^2
def recipe_batches(recipe, ingredients):
  if len(recipe.items()) != len(ingredients.items()):
    return 0

  # get all keys. so i dont have to worry about the order.
  ingredients_keys = list(recipe.keys())

  # if any value in recipe is greater than the corresponding value in ingredients,
  # return 0
  for k in ingredients_keys:
    if recipe[k] > ingredients[k]:
      return 0      

  # deduct each ingredient separately, 
  # then take the minimum amount of all of them
  # frequency counter.
  freq = {}
  for key in ingredients_keys:
    while ingredients[key] >= recipe[key]:
      if key in freq:
        freq[key] += 1
      else:
        freq[key] = 1
      ingredients[key] -= recipe[key]

  lowest = math.inf
  for val in freq.values():
    if val < lowest:
      lowest = val

  return lowest

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  # recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  # ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 50, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))