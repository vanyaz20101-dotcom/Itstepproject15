from colorama import init, Fore, Back, Style

init(autoreset=True)

print(Fore.GREEN + "Зелений текст")
print(Back.RED + "Фон червоний")
print(Style.BRIGHT + "Яскравий стиль")
print(Fore.BLUE + Back.YELLOW + "Комбінований стиль")
