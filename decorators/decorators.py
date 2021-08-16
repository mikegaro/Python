def se_educado(fn):
    def wrapper():
        print("Sabado, 14 de agosto del 2021 -> Iniciando programa\n\n ")
        fn()
        print("\n\nPrograma terminado...")
    return wrapper


def greet():
    print("Mi nombre es Colt!!")


def greet():
    print("Hola mundo")


def rage():
    print("Te odio Python!!!")


greet = se_educado(greet)
greet()

rage = se_educado(rage)

rage()

# Usando sintaxis de decorador con @
# En lugar de hacer miNombre = se_educado(miNombre)


@se_educado
def miNombre():
    print("Mi nombre es Miguel")


miNombre()
