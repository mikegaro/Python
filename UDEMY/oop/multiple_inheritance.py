class Aquatic:
    def __init__(self, name):
        self.name=name
    def swim(self):
        return f"{self.name} is swimming"
    def greet(self):
        return f"I am {self.name} of the sea"


class Ambulatory:
    def __init__(self,name) -> None:
        self.name=name

    def walk(self):
        return f"{self.name} is walking"
    
    def greet(self):
        return f"I am {self.name} of the land!"



class Penguin(Ambulatory, Aquatic):
    
    #Cada vez que se crea una clase, Python establece
    #algo llamado METHOD RESOLUTION ORDER, donde Python
    #decide cuales son los metodos que se llaman de que instancia
    #en caso que se este trabajando con multiple inheritance

    def __init__(self, name) -> None:
        super().__init__(name=name)

#Para conocer el MRO de la clase
print(Penguin.__mro__)
print(Penguin.mro())
help(Penguin)
#Estas son tres formas que te despliegan
#que clases padre se llaman primero para generar
#una instancia de una clase con herencia multiple


fish = Aquatic("Nemo")
mariposa = Ambulatory("Monarca")


pinguino = Penguin("Rico")