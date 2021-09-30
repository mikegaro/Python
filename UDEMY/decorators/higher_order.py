def sum(n, func):
    total = 0
    for num in range(n):
        total += func(num)
    return total


def square(x):
    return x*x


def cube(x):
    return x*x*x


print(sum(3, square))  # Aqui pasamos a square como un parametro

print(sum(3, cube))  # Aqui pasamos a cube como un parametro de la funcion
