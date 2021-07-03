class User:
    def __init__(self, nombre, apellido):
        # self se refiere a la instancia en especifico
        print("A new user has been created")
        self.name = nombre
        self.last = apellido

    def cambiarNombre(self, nombre):
        self.name = nombre

    def imprimirNombre(self):
        print("Mi nombre es " + self.name + " " + self.last)


user = User("Miguel", "Oñate")
user.imprimirNombre()
user.cambiarNombre("Edith")
user.imprimirNombre()
user.cambiarNombre("Miguel")
print(user.name)
