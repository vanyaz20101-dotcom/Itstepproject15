def calculator_decorator(func):
    def wrapper(expression):
        try:
            allowed = "0123456789+-*/(). "
            for char in expression:
                if char not in allowed:
                    raise ValueError("Wrong symbols!")
            result = func(expression)
            return f"Результат: {result}"
        except ZeroDivisionError:
            return "Error: you can't divide by 0!"
        except SyntaxError:
            return "Error: wrong syntax!"
        except ValueError as e:
            return f"Error: {e}"
        except Exception as e:
            return f"Unknown error: {e}"
    return wrapper
@calculator_decorator
def calculate(expression):
    return eval(expression)
print(calculate("2 + 3 * 4"))
print(calculate("10 / 0"))
print(calculate("5 +"))
print(calculate("__import__('os').system('cls')"))