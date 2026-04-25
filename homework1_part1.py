from datetime import datetime

class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year

    def show_info(self):
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.get_age()}")


class Driver(Person):
    def __init__(self, name, birth_year, license_number, experience):
        super().__init__(name, birth_year)
        self.license_number = license_number
        self.experience = experience

    def has_enough_experience(self):
        return self.experience > 2

    def show_info(self):
        super().show_info()
        print(f"Номер посвідчення: {self.license_number}")
        print(f"Стаж водіння: {self.experience} років")
        if self.has_enough_experience():
            print("Стаж достатній")
        else:
            print("Стаж недостатній")
        print("-" * 30)

driver1 = Driver("Іван", 2005, "AB1234", 3)
driver2 = Driver("Марія", 2008, "CD5678", 1)
driver3 = Driver("Олег", 2000, "EF9012", 5)

driver1.show_info()
driver2.show_info()
driver3.show_info()