def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args) if args else "None"
        kwargs_value = ", ".join(f"{k}:{v}" for k, v in kwargs.items()) if kwargs else "None"

        print(f"Calling {func.__name__} with args => {args_value} and kwargs => {kwargs_value}")

        return func(*args, **kwargs)

    return wrapper


@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")


@debug
def greetName(greeting="Hello"):
    print(f"{greeting}")


@debug
def hello():
    print("Hello world")


greet("Shashank", greeting="Yo")

hello()

greetName(greeting="Yo")
