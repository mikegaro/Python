def log_function_data(fn):
    def wrapper(*args, **kwargs):
        print(f"Hola{fn.__name__}")
        print(f"Esto es {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x, y):
    return x+y


print(add(10, 30))
