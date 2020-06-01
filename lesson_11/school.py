class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is {}. I am {} years old.".format(self.name, self.age))


class Student(Person):
    def __init__(self, name, age, speciality):
        Person.__init__(self, name, age)
        self.speciality = speciality

    def introduce(self):
        print("My name is {}. I am {} years old. I am a student of {}".format(self.name, self.age, self.speciality))
        
