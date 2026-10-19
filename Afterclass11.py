class Pet:
    def __init__(self, name, health):
        self.name = name
        self.__health = health

    def get_health(self):
        return self.__health

    def set_health(self, health):
        if health in ["Healthy", "Sick"]:
            self.__health = health

    def make_sound(self):
        print("The pet makes a sound.")

    def display(self):
        print(self.name, "-", self.get_health())


class Dog(Pet):
    def make_sound(self):
        print("Woof!")


class Cat(Pet):
    def make_sound(self):
        print("Meow!")


pets = [Dog("Buddy", "Healthy"), Cat("Whiskers", "Sick")]

pets[1].set_health("Healthy")

for pet in pets:
    pet.display()
    pet.make_sound()