class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1


p1 = Person("Chanuka")
print(p1.number_of_people)
p2 = Person("Dinuwan")
print(p1.number_of_people)

Person.number_of_people = 8
print(p1.number_of_people)
