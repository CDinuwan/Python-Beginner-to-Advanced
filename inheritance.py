class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("Null")


class Cat(Pet):
    def speak(self):
        print("Meow")


class Dog(Pet):  # Auto override that method
    def speak(self):
        print("Baw Baw")


class Fish(Pet):
    pass


p = Pet("Chanuka", 24)
p.show()

c = Cat("Puu", 19)
c.show()

d = Dog("buu", 25)
d.show()
d.speak()

f = Fish("Muu", 46)
f.speak()
