def add(*args, **kwargs):
    result = 0
    for arg in args + list(kwargs.values()):
        result += arg

    return result