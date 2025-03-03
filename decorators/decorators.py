import time

def timer(func):
    def wrapper(self, *args, **kwargs):
        start = time.time()
        result = func(self, *args, **kwargs)
        end = time.time()
        print(f" {func.__name__} Time elapsed: {end - start}")
        return result
    return wrapper

@timer
def ex(n):
    time.sleep(n)
 

ex(2)

