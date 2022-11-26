class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def go_to_work(self):
        print(f'{self.name} is going to work')

    def display_age(self):
        print(f'{self.name} is {self.age} years old')

    def celebrate_birthday(self):
        self.age += 1
        print(f'{self.name} is now {self.age} years old')

    def change_occupation(self, new_occup):
        self.occupation = new_occup


person2 = Person('Ikram', 20, 'student')
print(person2.display_age())
print(person2.celebrate_birthday())
print(person2.display_age())
