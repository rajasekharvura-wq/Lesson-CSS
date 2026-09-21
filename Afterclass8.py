class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def introduce(self):
        print(f"Hello, I am {self.name}, model {self.model}.")

my_robot = Robot("Sparky", "X-200")
my_robot.introduce()
