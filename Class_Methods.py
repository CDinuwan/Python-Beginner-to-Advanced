class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_Person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_Person(cls):
        cls.number_of_people += 1


p1 = Person("Chanuka")
p2 = Person("Dinuwan")

print(Person.number_of_people_())
