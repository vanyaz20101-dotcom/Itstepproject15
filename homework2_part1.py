result = []

def divider(a, b):
    if a < b:
        raise ValueError("a менше ніж b")
    if b > 100:
        raise IndexError("b більше 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")
    except IndexError as e:
        print(f"IndexError: {e}")
    except Exception as e:
        print(f"Інша помилка: {e}")

print(result)