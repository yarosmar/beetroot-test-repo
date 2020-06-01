class Dog:
    def __init__(self, age):
        self.age = age
        self.age_factor = 7

    def human_age(self):
        return self.age * self.age_factor
    
