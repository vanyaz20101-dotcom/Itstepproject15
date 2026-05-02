def decorator_v1(func):
    def wrapper():
        print("Calling decorator function")
        func()

    return wrapper


@decorator_v1
def sayHello():
    print("Hello")

sayHello()

proSayHello = decorator_v1(sayHello)
proSayHello()

def decorator_v2(func):
    def wrapper(*args, **kwargs):
        print("Calling decorator function")
        result = func(*args, **kwargs)
        return result

    return wrapper

def decorator_67(func):
    def wrapper(*args, **kwargs):
        print("Calling decorator function")
        result = func(*args, **kwargs)
        while result < 67:
            result += 1
        return result

    return wrapper

@decorator_67
def sum(a, b):
    return a + b

print(sum(4, 4))

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'time: {end - start}')
        return wrapper

    @timer
    def slow_func():
        time.sleep(1)

    slow.func()

    def counter():
        counter = 0
        for i in range(10000000):
            counter += 1

        return counter

    counter()

def add_method(cls):
    def say_hello(self):
        print("Hello from decorator")
    cls.say_hello = say_hello
    return cls

@add_method
class Person:
    pass

p1 = Person()
p1.say_hello()


def repeat(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            func(*args, **kwargs)
    return wrapper


@repeat
def say_goodbye():
    print("Goodbye!")

say_goodbye()

def to_upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@to_upper
def greet():
    return "hello world"

print(greet())