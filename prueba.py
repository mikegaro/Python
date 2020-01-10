from math import *

phrase = "Girafa Loca"
print(phrase)

personaje = "Tom"
edad = 50
macho = True

print("Hola a todos\n\"EDA\"")
print(phrase.lower())
print(phrase.upper())
print(phrase.lower().isupper())
print(len(phrase))

for i in range(0,len(phrase)):
    print(phrase[i])
print(phrase.index("a"))
print(phrase.replace("Girafa","Zebra"))
print(phrase)

print("\n\n\n")
print(3 +4*5)

mi_numero = -5.35

print(mi_numero)
print(abs(mi_numero))
print(pow(mi_numero,2))
print(round(mi_numero))

#ESTAS NECESITAN MATHPY
print(floor(mi_numero))
print(ceil(mi_numero))
print(sqrt(36))

nombre_ingresado = input("Ingresa tu nombre: ")
print("Hola" + nombre_ingresado + "!")
