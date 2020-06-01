class Person():

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print('Hello, my name is ' + self.firstname.title() + ' ' + self.lastname.title() + ' and I\'m ' + str(self.age) + '.')
    
persons_data = Person('carl', 'johnson', 26)
print(persons_data.talk())


