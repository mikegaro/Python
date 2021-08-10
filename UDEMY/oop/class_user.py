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


# PYHON NO MANEJA EL CONCEPTO DE ATRIBUTOS PRIVADOS, A CONTINUACION SE MUESTRA UNA 
# CONVENCION QUE HACEN LOS PROGRAMADORES PARA INDICAR QUE NO SE DEBERIA ACCESAR AL ATRIBUTO
# SIN EMBARGO NO PASA NADA SI SE MANIPULA ESE ATRIBUTO "PRIVADO"

class Persona:
    def __init__(self, nombre="Miguel", curp="12354"):
        self.nombre=nombre #ESTA ES UNA ATRIBUTO PUBLICO PORQUE NO TIENE _
        self._curp=curp #ESTE ES UN ATRIBUTO PRIVADO POR EL _ AL INICIO DE curp
        self.__mensaje="este es un mensaje"
    
p = Persona()
print(p.__mensaje)

