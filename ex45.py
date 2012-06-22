## Animal is-a object (confusing, yes_ Look at the xtra credit
class Animal(object):

    def __init__(self, age):
        self.age = age

## dog is an animal
class Dog(Animal):

    def __init__(self, name):
        ##self has a name
        self.name = name

## Cat is an animal
class Cat(Animal):

    def __init__(self, name):
        ## self has a name
        self.name = name

## ??
class Person(object):

    def __init__(self, name):
        ## self has a name
        self.name = name

        ## Person has a pet of some kind
        self.pet = None

## Employee is a person
class Employee(Person):

    def __init__(self, name, salary):
        ##magic
        super(Employee, self).__init__(name)
        ## employee has a salary
        self.salary = salary

## fish is an object
class Fish(object):
    pass

## salmon is a fish
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass

animal = Animal(8)

##rover is a dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

##mary is a person
mary = Person("Mary")

## mary has a pet named satan
mary.pet = satan

##frank is an employee
frank = Employee("Frank", 120000)

##frank has a pet named rover
frank.pet = rover

##flipper is a fish
flipper = Fish()

##crouse is a salmon
crouse = Salmon()

##harry is a halibut
harry = Halibut()


        
