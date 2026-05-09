import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/"

def get_rates(base_currency):
    try:
        response = requests.get(API_URL + base_currency.upper())
        response.raise_for_status()
        data = response.json()
        return data["rates"]
    except requests.exceptions.RequestException as error:
        print("Помилка при отриманні курсу валют:")
        print(error)
        return None

def convert_currency(amount, from_currency, to_currency):
    rates = get_rates(from_currency)

    if rates is None:
        return

    to_currency = to_currency.upper()

    if to_currency not in rates:
        print("Невідома валюта.")
        return

    result = amount * rates[to_currency]
    print(f"\n{amount} {from_currency.upper()} = {result:.2f} {to_currency}")

def main():
    print("=== Конвертер валют ===")

    try:
        amount = float(input("Введіть суму: "))
        from_currency = input("З якої валюти (наприклад USD): ")
        to_currency = input("В яку валюту (наприклад EUR): ")

        convert_currency(amount, from_currency, to_currency)

    except ValueError:
        print("Помилка: введіть правильне число.")

if __name__ == "__main__":
    main()