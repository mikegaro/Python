def add_positive_numbers(x, y):
    assert x > 0 and y > 0
    return x+y

# Usando assert podemos evaluar las variables de manera rapida
# y eficaz


add_positive_numbers(1, 1)  # Sin problemas
add_positive_numbers(1, -1)  # AssertError

# WARNING: Si un archivo de Python se corre con la flag -O, assertions
#          no sera evaluado.
