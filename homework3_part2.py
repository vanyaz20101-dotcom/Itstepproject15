import logging

logging.basicConfig(level=logging.ERROR, filename='error.log', format="%(asctime)s - %(levelname)s - %(message)s")

try:
    number1 = int(input("Enter first number:" ))
    number2 = int(input("Enter second number:"))

    result = number1 / number2
except Exception as error:
    logging.error(f"An error occured: {error}")
    print("Error occured! Details at error.log")

