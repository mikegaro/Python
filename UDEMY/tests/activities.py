# Unit testing

# Test smallest parts of an application in asolation (e.g units)
# Good candidates for unit testing: individual classes, modules, or functions.
# Bad candidates for unit testing: an entire application, dependencies across
# several classes or modules.


def eat(food, is_healthy):
    ending = "because YOLO!"
    if is_healthy:
        ending = "because my body is a temple"
    return f"Im eating {food}, {ending}"


def nap(num_hours):
    if num_hours > 2:
        return f"Ugh I overslept. I didnt mean to nap"
    return f"Im feeling refreshed after my 1 hour nap"
