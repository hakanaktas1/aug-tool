import random

class Parent:
    random_value = None

    @classmethod
    def generate_random_value(cls):
        cls.random_value = random.randint(0, 10)

class FirstSubclass(Parent):
    def __init__(self):
        super().__init__()
        self.update_random_value()

    def update_random_value(self):
        self.generate_random_value()

class SecondSubclass(Parent):
    def __init__(self):
        super().__init__()

    def get_random_value(self):
        return self.random_value

# Creating instances of the subclasses
first = FirstSubclass()
second = SecondSubclass()

# Accessing the random value in the second subclass
print(second.get_random_value())
