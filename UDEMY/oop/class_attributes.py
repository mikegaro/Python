class User:

    active_users=0  # ESTE ES EL ATRIBUTO DE LA CLASE Y ES UNIVERSAL NO IMPORTA LAS INSTANCIAS QUE SE CREE
                    # ESTE ATRIBUTO ES UNICO Y EXCLUSIVO DE LA CLASE


    @classmethod #METODOS EXCLUSIVOS DE LA CLASE, NO DE LA INSTANCIA
    def display_usuarios_activos(cls):
        print(cls)
        return f"Hay {cls.active_users} usuarios activos"

    @classmethod
    def from_string(cls, data):#METODOS EXLCUSIVOS DE LA CLASE, NO DE LA INSTANCIA
        first,last = data.split(",")
        return cls(first, last) #cls refiere a la clase, es decir, nos regresa una instancia

    def __init__(self, nombre, apellido):
        # self se refiere a la instancia en especifico
        self.name = nombre
        self.last = apellido
        User.active_users+=1
        print(f"{self.name} ha sido creado")
        print(f"\nHasta el momento hay {str(User.active_users)} usuarios activos\n")

    def __repr__(self):
        return f"Esta instancia es {self.name}"

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

print(User.display_usuarios_activos())

user_tres = User("Fernanda", "Oñate")

user_cuatro = User("Miguel", "Elchido")

print(User.display_usuarios_activos())

user_cinco = User.from_string("Miguel,Onate")

print(User.display_usuarios_activos())


#ESTO ES LO QUE PASA SI ESTABLECEMOS EL METODO __repr__
j = User("Luis Miguel", "jeje")
print(j) # En lugar de que nos aparezca "<__main__.User at 0x129347>" 
         # nos aparece algo personalizado


class Moderador(User):
    def __init__(self, nombre, apellido, community):
        super().__init__(nombre, apellido)
        self.community = community

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community"

pepe = Moderador("PEPE", "FLORES", "Ingenierios UNAM")

print(pepe.imprimirNombre())
print(pepe.community)