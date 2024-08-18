import time
from functools import wraps

def cache(func):
    cache_value = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Convert kwargs to a sorted tuple of key-value pairs to ensure immutability
        kwargs_tuple = tuple(sorted(kwargs.items()))
        key = (args, kwargs_tuple)
        if key in cache_value:
            return cache_value[key]
        result = func(*args, **kwargs)
        cache_value[key] = result
        return result

    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

# Testing the function
print(long_running_function(2, 3))  # This will take some time (4 seconds)
print(long_running_function(2, 3))  # This will return instantly from the cache
print(long_running_function(4, 8))  # This will take some time (4 seconds)
