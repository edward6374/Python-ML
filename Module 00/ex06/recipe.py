import sys

sentences = {
    "Welcome" : "Welcome to the Python CookBook!",
    "Options" : """List of available options:
    1:\tAdd a recipe
    2:\tDelete a recipe
    3:\tPrint a recipe
    4:\tPrint the CookBook
    5:\tQuit
    help: Print all the options""",
    "Select" : "Please select an option:\n",
    "Wrong_opt" : "Wrong option, please select one of the options available",
    "Enter_name" : "Enter a name for the recipe:",
    "Enter_ingr" : "Enter all the ingredients one by one:",
    "Enter_type" : "Enter a meal type:",
    "Enter_prep" : "Enter a preparation time:",
    "Recipe_created" : "Recipe created successfully",
    "Delete_name" : "Please enter the recipe name to delete:",
    "Delete_succ" : "Recipe deleted correctly!",
    "Delete_fail" : "Recipe not found!",
    "Print_name" : "Please enter a recipe name to get its details:",
    "Print_succ" : "Recipe for",
    "Print_book" : "All the recipes in the CookBook below:",
    "Quit" : "Bye bye!"
}

cookbook = {
    "Bocadillo" : {
        "ingredients" : ["jamon", "pan", "queso", "tomate"],
        "meal" : "almuerzo",
        "prep_time" : 10,
        },
    "Tarta" : {
        "ingredients" : ["harina", "azucar", "huevos"],
        "meal" : "postre",
        "prep_time" : 60,
        },
    "Ensalada" : {
        "ingredients" : ["aguacate", "rucula", "tomates", "espinacas"],
        "meal" : "almuerzo",
        "prep_time" : 15,
        }
}

def add_recipe():
    print("Add recipe")

def delete_recipe():
    print("Delete recipe")

def print_recipe():
    print("Print recipe")

def print_cookbook():
    print("Print cookbook")

if __name__ == "__main__":
    control = True
    print(sentences["Welcome"])
    print(sentences["Options"])
    while (control):
        options = input(sentences["Select"])
        if options == "1":
            add_recipe()
        elif options == "2":
            delete_recipe()
        elif options == "3":
            print_recipe()
        elif options == "4":
            print_cookbook()
        elif options == "5":
            control = False
        elif options == "help":
            print(sentences["Options"])
        else:
            print(sentences["Wrong_opt"])
