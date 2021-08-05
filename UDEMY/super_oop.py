class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self, sound):
        print(f"Este animal dice {sound}")

class Cat(Animal):
    def __init__(self, name, species, breed, toy):
        super().__init__(name, species="Cat") #<--- Gracias a super() python sabe que nos estamos refierendo a la clase padre
        #Animal.__init__(self, name, species): <--- Por lo tanto ya no tenemos que hacer esto
        self.breed = breed
        self.toy = toy
        #Dado que cat es heredado por Animal, Cat tambien tiene la funcion make_sound

        
    def play(self):
        print(f"{self.name} plays with {self.toy}")