class GotCharacter:

    def __init__(self, first_name = None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    
    def __init__(self, first_name = None, is_alive=True):
        super().__init__(first_name = first_name, is_alive = is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is coming"

    def print_house_words(self):
        return self.house_words

    def die(self):
        self.is_alive = False

class Lannister(GotCharacter):
    
    def __init__(self, first_name = None, is_alive = True):
        super().__init__(first_name = first_name, is_alive = is_alive)
        self.family_name = "Lannister"
        self.house_words = "We will conquer the world"

    def print_house_words(self):
        return self.house_words

    def die(self):
        self.is_alive = False

arya = Stark("Arya")
print(arya.__dict__)
arya.print_house_words()
print("Alive:", arya.is_alive)
arya.die()
print(arya.__dict__)
print("Alive:", arya.is_alive)

tywin = Lannister("Tywin")
print(tywin.__dict__)
tywin.print_house_words()
print("Alive:", tywin.is_alive)
tywin.die()
print(tywin.__dict__)
print("Alive:", tywin.is_alive)
