class Robot:
    def __init__(self, name, model, task):
        self.name = name
        self.model = model
        self.task = task
    def introduce(self):
        print(f"Hello, I am {self.name}, a {self.model} model.")
        print(f"My primary purpose is {self.task}.")

my_robot = Robot("Astra", "v2.0", "assisting with complex coding tasks")
my_robot.introduce()

