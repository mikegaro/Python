

def shout(fn):
    # <- Con esto aseguramos que se puedan meter tantos parametros como se desee
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper


#  def shout(fn): <- Si ponemos este codigo, el decorador solo va a poder aceptar un parametro
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper


@shout
def greet(name):
    return f"Hola, soy {name}"


@shout
def order(main, side):
    return f"Hola, quiero {main}, con un poco de {side}"
