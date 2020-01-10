amigos = ["Kevin","Karen","Brayan"]

print(amigos)

print(amigos[0] + "\n")
#Kevin

print(amigos[1:])
#['Karen', 'Brayan']

print(amigos[0:1])
#Kevin

amigos[1] = "Miguel"
print(amigos)
#['Kevin', 'Miguel', 'Brayan']

amigos.append("DIEGOL")
print(amigos)
#['Kevin', 'Miguel', 'Brayan', 'DIEGOL']

amigos.insert(1,"Kelly")
print(amigos)
#['Kevin', 'Kelly', 'Miguel', 'Brayan', 'DIEGOL']

amigos.remove("Brayan")
print(amigos)
#['Kevin', 'Kelly', 'Miguel', 'DIEGOL']

amigos.pop()
print(amigos)
#['Kevin', 'Kelly', 'Miguel']

numeros_de_la_suerte = [1,2,3,4,5,6]
amigos.extend(numeros_de_la_suerte)
print(amigos)
 #['Kevin', 'Kelly', 'Miguel', 1, 2, 3, 4, 5, 6]

print(amigos.index("Kelly"))
#Kelly se encuentra en el indice 1

print(amigos.count("Miguel"))
#Miguel se encuentra 1 ves en el arreglo

numeros_de_la_suerte.reverse()
print(numeros_de_la_suerte)
#[6, 5, 4, 3, 2, 1]

numeros_de_la_suerte.sort()
print(numeros_de_la_suerte)
#[1, 2, 3, 4, 5, 6]

#En python3 se puede utilizar 'amigos.copy()'
amigos2 = list(amigos)
amigos3 = amigos[:]
print(amigos2)
print(amigos3)
#Dos formas de copiar los elementos de una lista
#['Kevin', 'Kelly', 'Miguel', 1, 2, 3, 4, 5, 6]
#['Kevin', 'Kelly', 'Miguel', 1, 2, 3, 4, 5, 6]

#En python3 se puede utilizar 'amigos.clear()'
del amigos[:]
amigos2[:] = []
#Dos formas de eliminar todos los elementos
print(amigos)
#[]
print(amigos2)
#[]

lista_de_lista = [["Vento","March","Sentra"],["A1","A3","A5"]
                  ,["Golf","Passat","Polo"]]
print(lista_de_lista)
#[['Vento', 'March', 'Sentra'], ['A1', 'A3', 'A5'], ['Golf', 'Passat', 'Polo']]


la_mejor_marca = [lista_de_lista[1][:]]
print(la_mejor_marca)
#[['A1', 'A3', 'A5']]

el_mejor_auto = [lista_de_lista[2][0]]
print(el_mejor_auto)
#['Golf']

losMasFeosPorMarca = lista_de_lista[:][2]
print(losMasFeosPorMarca)
#['Golf', 'Passat', 'Polo']
