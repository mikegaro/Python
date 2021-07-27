class User:

    active_users=0  # ESTE ES EL ATRIBUTO DE LA CLASE Y ES UNIVERSAL NO IMPORTA LAS INSTANCIAS QUE SE CREE
                    # ESTE ATRIBUTO ES UNICO Y EXCLUSIVO DE LA CLASE

    def __init__(self, nombre, apellido):
        # self se refiere a la instancia en especifico
        self.name = nombre
        self.last = apellido
        User.active_users+=1
        print(f"{self.name} ha sido creado")
        print(f"\nHasta el momento hay {str(User.active_users)} usuarios activos\n")

    def cambiarNombre(self, nombre):
        self.name = nombre

    def imprimirNombre(self):
        print("Mi nombre es " + self.name + " " + self.last)

    def borrarUsuario(self):
        User.active_users-=1
        print(f"{self.name} ha sido borrado")
        print(f"\nHasta el momento hay {User.active_users} usuarios activos")

user = User("Miguel", "Oñate")

user_dos = User("Fernanda", "Garcia")

user_dos.borrarUsuario()
