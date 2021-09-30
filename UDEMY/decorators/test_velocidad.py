from time import time


def speed_test(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Time Elapsed: {end_time-t1}")
        return result
    return wrapper


@speed_test
def suma_numeros():
    return sum(x for x in range(50000000))


@speed_test
def suma_numeros_lista():
    return sum([x for x in range(50000000)])


print(suma_numeros())
print(suma_numeros_lista())
