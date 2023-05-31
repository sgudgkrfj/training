import random



class Animal:
    def __init__(self, species, name, age, health, hunger, happiness):
        super().__init__()
        self.species = species
        self.name = name
        self.age = age
        self.health = health
        self.hunger = hunger
        self.happiness = happiness

    def grow(self):
        self.age += 1
        self.health += random.randint(0, 10)
        self.hunger = random.randint(0, 10)
        self.happiness = random.randint(0, 10)

    def eat(self):
        if self.hunger>=6:

            self.hunger += random.randint(1, 5)
            self.happiness -= random.randint(1, 5)
            self.hunger -= random.randint(1, 5)
        else:
            return self.name, "не голодний"

    def play(self):
        self.happiness += random.randint(1, 5)




    def __str__(self):
        return f"Ім'я: {self.name}, вік: {self.age}, здоров'я: {self.health}, голод: {self.hunger}, щастя:{self.happiness}"

class Zoo:
    def __init__(self):
        super().__init__()
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)



    def remove_animal(self, animal):
        removed_animal = next(filter(lambda j: j.species == animal.species and
                                                j.name == animal.name and
                                                j.age == animal.age and
                                                j.health == animal.health and
                                                j.hunger == animal.hunger and
                                                j.happiness == animal.happiness, self.animals), None)

        if removed_animal is not None:
            self.animals.remove(removed_animal)
        else:
            return f"Тварина {removed_animal} відсутня в списку"

    def feed_all(self):
        for animal in self.animals:
            animal.eat()

    def play_with(self, animal):
        if animal in self.animals:
            animal.play()

    def grow_all(self):
        for animal in self.animals:
            animal.grow()

monkey1 = Animal("горила", "даша", 10, 40, 25, 15)
monkey2 = Animal("горила", "маша", 10, 40, 25, 15)
monkey3 = Animal("горила", "саша", 10, 40, 25, 15)
monkey4 = Animal("горила", "гріша", 10, 40, 25, 15)
monkey5 = Animal("горила", "дмитро", 10, 40, 25, 15)
monkey6 = Animal("горила", "костя", 10, 40, 25, 15)

zoo = Zoo()
zoo.add_animal(monkey1)
zoo.add_animal(monkey2)
zoo.add_animal(monkey3)
zoo.add_animal(monkey4)
zoo.add_animal(monkey5)
zoo.add_animal(monkey6)

for days in range(1,11):
    zoo.feed_all()
    zoo.grow_all()
    a = random.choice(zoo.animals)
    zoo.play_with(a)
    if days == 5:
        zoo.remove_animal(monkey5)
    if days == 9:
        zoo.remove_animal(monkey2)
    print(f"День №{days}")
    for animal in zoo.animals:
        print(animal)

