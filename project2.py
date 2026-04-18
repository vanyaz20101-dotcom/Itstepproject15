import random


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.alive = True

    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}"

    def eat(self):
        print("Котик їсть")
        self.hunger -= 15
        self.happiness += 5
        self.energy += 5

    def sleep(self):
        print("Котик спить")
        self.energy += 15
        self.hunger += 5

    def play(self):
        print("Котик грається")
        self.happiness += 10
        self.energy -= 10
        self.hunger += 5

    def scratch(self):
        print("Котик дере диван")
        self.happiness += 5
        self.energy -= 5

    def end_of_day(self):
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}")

    def check_alive(self):
        if self.hunger >= 100:
            print("Котик дуже голодний...")
            self.alive = False
        elif self.energy <= 0:
            print("Котик втомився...")
            self.alive = False
        elif self.happiness <= 0:
            print("Котик сумний...")
            self.alive = False

    def live(self, day):
        if not self.alive:
            print("Котик більше не може жити...")
            return

        print(f"\nDay {day} життя котика {self.name}")

        action = random.randint(1, 4)

        if action == 1:
            self.eat()
        elif action == 2:
            self.sleep()
        elif action == 3:
            self.play()
        elif action == 4:
            self.scratch()

        self.end_of_day()
        self.check_alive()


tom = Cat("Tom", 3)

for day in range(1, 31):
    if not tom.alive:
        break
    tom.live(day)