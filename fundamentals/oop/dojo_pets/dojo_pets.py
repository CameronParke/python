class Pet:
    def __init__(self, name, type, tricks, health, energy, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.health += 10
        self.energy += 5
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print(self.noise)

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play(self)
        return self

    def feed(self):
        self.pet.eat(self)
        return self
    
    def bathe(self):
        self.pet.noise(self)
        return self        
        
cameron = Ninja("Cameron", "Parke", "Churu Squeezes", "Kibbies", Pet)
Bubbins = Cat("Bubber", "Tuxedo", "Makes Hair Ties Disappear", 100, 50, "Meow")
Buddy = Dog("Budweiser", "Black Lab Mix", "Break Free", 100, 85, "Bork")


# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method