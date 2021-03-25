class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_age(self):
        value = 0
        for student in self.students:
            value += student.get_age()

        return value/len(self.students)


s1 = Student("Chanuka", 24)
s2 = Student("Dilini", 21)
s3 = Student("Time", 18)

course = Course("OOP", 10)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.students[0].name)
print(course.get_average_age())
