def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def greet(name,g):
    print(f"{g},{name}")


greet("ok","ok")