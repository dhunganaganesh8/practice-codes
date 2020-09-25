## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a animal and has-a __init__.
class Dog(Animal):

    def __init__(self, name):
        ##Dog has-a name
        self.name = name

## Cat is-a Animal and has-a __init__ function.
class Cat(Animal):

    def __init__(self, name):
        ##  Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ##Person has-a name.
        self.name = name

        ##Person has-a pet of some kind.
        self.pet = None

    def info(self):
        print("{} keeps {} as his pet.".format(self.name, self.pet))

## Employee is-a Person.
class Employee(Person):

    def __init__(self, name, salary):
        ##
        super(Employee, self).__init__(name)
        ##Employee has-a salary of some value.
        self.salary = salary

    def status(self):
        print('The name of the Employee is {}.'.format(self.name))

        if int(self.salary) > 50000:
            print("The employee has a high salary.")
        else:
            print("The employee has a low salary.")

##Fish is-a object.
class Fish(object):
    pass

##Salmon is a Fish.
class Salmon(Fish):
    pass

##Halibut is-a Fish.
class Halibut(Fish):
    pass


## rover is-a Dog.
rover = Dog("Rover")

##satan is-a cat.
satan = Cat('Satan')

## mary is-a person.
mary = Person(input("Enter the name for the person: "))
mary.info()

##mary has-a pet.
mary.pet = satan

## Frank is-a Employee.
frank = Employee(input("Enter name of the Employee: "), input("Enter his salary: "))
frank.status()
mary.info()
frank.info()

## frank has-a pet.
frank.pet = rover
frank.info()
## flippper is-a Fish.
flipper = Fish()

##crouse is-a Salmon.
crouse = Salmon()

##harry is-a Halibut.
harry = Halibut()
