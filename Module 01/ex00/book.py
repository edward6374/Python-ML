from datetime import datetime

class Book:

    def __init__(self, name, last_update, creation_date, recipes_list):
        if type(name) is not str:
            raise ValueError("Name has to be a string")
        if type(last_update) is not datetime:
            raise ValueError("Last update has to be a datetime")
        if type(creation_date) is not datetime:
            raise ValueError("Creation date has to be a datetime")
        if type(recipes_list) is not dict:
            raise ValueError("Recypes list has to be a dictionary")
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        return next((elem for list_recipes in self.recipes_list.values() for elem in list_recipes if elem.name == name), None)

    def get_recipes_by_type(self, recipe_type):
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe):
        if recipe.recipe_type not in self.recipes_list.keys():
            self.recipes_list[recipe.recipe_type] = [recipe]
        else:
            self.recipes_list[recipe.recipe_type].append(recipe)
