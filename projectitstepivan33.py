class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

class Zoo:
    def __init__(self):
        self.name = 'Zoo'
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def del_animal(self, animal):
        for animal in self.animals:
            if animal.name == animal.name:
                self.animals.remove(animal)
                return
        print(f"Тварину '{animal.name}' не знайдено")

    def show_animals(self):
        for animal in self.animals:
            print(animal)


zoo = Zoo()
zoo.add_animal(Animal(name="joe", age=20))
zoo.add_animal(Animal(name="barsik", age=10))
zoo.show_animals()

zoo.del_animal("joe")
zoo.show_animals()
