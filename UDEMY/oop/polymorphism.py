class Animal():
    def speak(self):
        raise NotImplementedError


class Perro(Animal):
    def speak(self):
        return "woof"


class Cat(Animal):
    def speak(self):
        return "miau"


class Fish(Animal):
    pass


d = Perro()
print(d.speak())
print(d.speak())

# En este caso la funcion speak esta declara tanto en la clase
# padre y en la clase hijo

# Cada subclase tiene una implementacion diferente de speak

# Usando method overriding, se puede saltar la implementacion de metodo padre

# Otra forma de polimorfismo es que la misma operacion funcione en diferentes objetos
# Ejemplo: 8+2 y "8"+"2". El signo + puede operar en diferentes objetos


class Human:
    def __init__(self, first, last, age) -> None:
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Mi nombre es {self.first} {self.last}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="Bebe", last=self.last, age=0)
        return "Esto no se puede añadir"


j = Human("Miguel", "Garcia", 21)
k = Human("Kevin", "Jones", 49)

print(j)
print(len(j))
print(k)
print(j+k)
