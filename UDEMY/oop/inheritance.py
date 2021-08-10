class Animal:
    cool=True

    def make_sound(self, sound):
        print(f"El animal hace {sound}")

#Aqui se indica que Cat tendra la herencia de Animal
class Cat(Animal):
    pass


garfield = Cat()
