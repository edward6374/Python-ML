from book import Book
from recipe import Recipe
from datetime import datetime

first_book = Book("First", datetime.now(), datetime.now(), {})
tortilla = Recipe("Tortilla", 2, 25, ["patatas", "huevos"], "Muy buena", "comida")
print(str(tortilla), end="\n\n")
print("Type:", type(tortilla), end="\n\n")
first_book.add_recipe(tortilla)
print("Comida:", ", ".join(elem.name for elem in first_book.get_recipes_by_type("comida")), end="\n\n")
recipe = first_book.get_recipe_by_name("Tortilla")
print("Recipe:\n", str(recipe), end="\n\n")
pasta_pesto = Recipe("Pasta al pesto", 1, 15, ["pasta", "pesto", "grana"], "Espectacular", "comida")
print(str(pasta_pesto), end="\n\n")
first_book.add_recipe(pasta_pesto)
print("Comida:", ", ".join(elem.name for elem in first_book.get_recipes_by_type("comida")), end="\n\n")
