class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = max(age,0) #Para uso interno de la clase solamente debido al _

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        self._age = max(new_age,0)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):  #El nombre del decorator tiene que ser el mismo que la
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Edad no puede ser negativa")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")

    #AMBOS METODOS SE LLAMAN AGE, UNO QUE REGRESA EL VALOR Y OTRO QUE LO IMPLEMENTA
    #EN LUGAR DE TENER QUE CREAR METODOS COMO OBTENER_NOMBRE Y SET_NOMBRE


#EL PUNTO DE todo ESTO SEGUIR LA CONVENCION QUE SE TIENE SOBRE LOS ATRIBUTOS "privados" ._atributo 

jane = Human("Jane", "Goodall", 34)
#print(jane.get_age())
#jane.set_age(50)      <---- ESTO YA NO ES NECESARIO PORQUE YA LO ESTABLECIMOS COMO PROPERTY
#print(jane.set_name())
print(jane.age)
jane.age = 20   #    <---- GRACIAS A LAS PROPERTIES PODEMOS SIMPLEMENTE LEER Y ESCRIBIR COMO UNA SIMPLE VARIABLE
print(jane.age)

