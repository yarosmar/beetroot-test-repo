from abc import *

class Animal(metaclass=ABCMeta):
    def __init__(self):
        self.legs = 0

    @abstractmethod
    def talk(self):
        print('Voice!')


class Dog(Animal):
    def __init__(self, age, name):
        Animal.__init__(self)
        self.name = name
        self.age = age

    def talk(self):
        print('Woof, woof!')


class Cat(Animal):
    def __init__(self, age, name):
        Animal.__init__(self)
        self.name = name
        self.age = age

    def talk(self):
        print('Meow!')
 
        
