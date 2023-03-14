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
    "Select" : "\nPlease select an option:\n>> ",
    "Wrong_opt" : "Wrong option, please select one of the options available",
    "Enter_name" : ">>> Enter a name for the recipe:\n",
    "Enter_ingr" : ">>> Enter all the ingredients one by one:",
    "Enter_type" : ">>> Enter a meal type:\n",
    "Enter_prep" : ">>> Enter a preparation time:\n",
    "Recipe_created" : "\nRecipe created successfully\n",
    "Delete_name" : ">>> Please enter the recipe name to delete:\n",
    "Delete_succ" : "\nRecipe deleted correctly!\n",
    "Delete_fail" : "\nRecipe not found!\n",
    "Print_name" : ">>> Please enter a recipe name to get its details:\n",
    "Print_succ" : "\nRecipe for",
    "Print_book" : "All the recipes in the CookBook below:\n",
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
    control = True
    name = input(sentences["Enter_name"])
    ingr = []
    print(sentences["Enter_ingr"])
    while control:
        one = input()
        if one is "":
            control = False
        else: 
            ingr.append(one)
    control = True
    typo = input(sentences["Enter_type"])
    while control:
        prep = input(sentences["Enter_prep"])
        if not prep.strip().isdigit():
            print("Insert a valid value!\n")
        else:
            control = False
    new_dict = {
        "ingredients" : ingr,
        "meal" : typo,
        "prep_time" : int(prep)
    }
    cookbook[name] = new_dict
    print(sentences["Recipe_created"])

def delete_recipe():
    name = input(sentences["Delete_name"])
    if name not in cookbook.keys():
        print(sentences["Delete_fail"])
    else:
        del cookbook[name]
        print(sentences["Delete_succ"])

def print_recipe():
    name = input(sentences["Print_name"])
    if name not in cookbook.keys():
        print(sentences["Delete_fail"])
    else:
        print(sentences["Print_succ"], name, ":")
        for i, l in cookbook[name].items(): 
            print("  ", i, ": ", end="")
            if type(l) is list:
                print(", ".join(l))
            else:
                print(l)
    print()

def print_cookbook():
    print(sentences["Print_book"])
    for i, j in cookbook.items():
        print(i)
        for k, l in j.items():
            print("  ", k, ": ", end="")
            if type(l) is list:
                print(", ".join(l))
            else:
                print(l)
        print()
    print()

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
            print(sentences["Quit"])
            control = False
        elif options == "help":
            print(sentences["Options"])
        else:
            print(sentences["Wrong_opt"])
