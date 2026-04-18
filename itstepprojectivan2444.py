class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, poroda):
        super().__init__(name, age)
        self.poroda = poroda
    def speak(self):
        print("gav gav")

class Cat(Animal):
    def __init__(self, name, age, hp):
        super().__init__(name, age)
        self.hp = hp
    def speak(self):
        print("meow")

dog1 = Dog('Sharik', 20, poroda=123)

print(dog1.name)
dog1.speak()

class Cat(Animal):
    def speak(self):
        print("meow")

cat1 = Cat('Barsik', 15)
print(cat1.name)
cat1.speak()



