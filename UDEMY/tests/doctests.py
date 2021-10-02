def add(a, b):
    """
    >>> add(2,3)
    5
    >>> add(100,200)
    300
    """
    return a+b

# Para que el tests que esta en el docstring se ejecute, se escribe en terminal
# python -m doctest -v doctests.py


def double(values):
    """double the values in a list

    >>> double([1,2,3,4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a','b','c'])
    ['aa', 'bb', 'cc']

    Args:
        values (list): it can be anything except bool
    """
    return [2*element for element in values]

# python -m doctest -v doctests.py
