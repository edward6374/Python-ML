class Recipe:

    def __init__(self, name, cook_lvl, cook_time, ingr, descr, rec_type):
        if type(name) is not str:
            raise ValueError("Name has to be a string")
        if type(cook_lvl) is not int or (int(cook_lvl) < 1 or int(cook_lvl) > 5):
            raise ValueError("Cooking level has to be int and between 1 and 5")
        if type(cook_time) is not int:
            raise ValueError("Cooking time has to be int")
        if type(ingr) is not list:
            raise ValueError("Ingredient list has to be a list")
        if descr is not "" and type(descr) is not str:
            raise ValueError("Description has to be a string")
        if type(rec_type) is not str:
            raise ValueError("Recipe type has to be a string")
        self.name = name
        self.cooking_lvl = int(cook_lvl)
        self.cooking_time = int(cook_time)
        self.ingredients = ingr
        self.description = descr
        self.recipe_type = rec_type

    def __str__(self):
        txt = ""
        txt += "\rName: " + self.name + "\n"
        txt += "Cooking level: " + str(self.cooking_lvl) + "\n"
        txt += "Cooking time: " + str(self.cooking_time) + "\n"
        txt += "Ingredients: " + ", ".join(item for item in self.ingredients) + "\n"
        txt += "Description: " + self.description + "\n"
        txt += "Recype type: " + self.recipe_type
        return txt
