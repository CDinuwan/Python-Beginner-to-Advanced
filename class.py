class Dog:
    def __init__(self, name):  # Constructor
        self.name = name

    def bark(self):
        print("bark")

    def meow(self):
        return 1

    def get_name(self):
        return self.name


d = Dog("Chanuka")
d2 = Dog("Dinuwan")
print(d2.name)
d.meow()
Dog.bark(self="")
print(Dog.meow(5))

print(type(d))

print(d.get_name())
