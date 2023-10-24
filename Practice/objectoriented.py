class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f'Hi! I am {self.name}')


person1 = Person("Ralph")
person1.talk()

person2 = Person('Raven')
person2.talk()

#Inheritance

class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('Woof!')


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()
dog1.bark()

