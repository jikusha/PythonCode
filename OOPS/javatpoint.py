class Employee:
    count = 0 # class variable. It is exchanged by all the instances

    def __init__(self, emp_id, bu): # constructor used to initialize an object
        self.emp_id = emp_id # instance variable
        self.bu = bu
        Employee.count+=1 # accessing the class variable using class name

    def display(self): #method is a function associated with an object
        print("Hi", self.emp_id, self.bu)


e1 = Employee(429877, 'FSDC') #an instance of the class # constructor called
e1.display() #method is associated with e1 object

#built-in class methods

print(getattr(e1, 'emp_id'))
setattr(e1, 'emp_id', 432321)
print(getattr(e1, 'emp_id'))
print(hasattr(e1, 'bu'))
delattr(e1, 'bu')
print(hasattr(e1,'bu'))

#built-in class methods

e2 = Employee(429878, 'ASDC') #an instance of the class
e2.display() #method is associated with e2 object

# built-in class attributes

print(e2.__doc__) #It contains a string which has the class documentation
print(e2.__dict__) # It provides the dictionary containing the information about the class namespace.
print(e2.__module__) # module where class is defined

print(Employee.count) #class variable

class Animal:
    def __init__(self):
        print("First Constructor")

    def __init__(self):
        print("Second Constructor")

    def speak(self):
        print("Animal can speak")

class Dog(Animal): #inheritance
    def bark(self):
        print("Dog can bark")

class Puppy(Dog): #multi-level inheritance
    def bark(self):
        print("Puppy can bark but not like Dog")


a = Animal() #always calls the last constructor

d = Dog()

d.bark()
d.speak() # inherited parent class method

p = Puppy()
p.speak()
p.bark() #method inheritance overriding


# In Python multiple inheritance is possible

class TerrestrialAnimal(Animal):
    def jump(self):
        print("jumps in land")

class AquaticAnimal(Animal):
    def swim(self):
        print("swims in water")

class Frog(TerrestrialAnimal, AquaticAnimal): #multiple inheritance
    pass

f = Frog()
f.jump()
f.swim()
f.speak()

# issubclass method
print(issubclass(TerrestrialAnimal, Animal))
print(issubclass(Puppy, Animal))
print(issubclass(AquaticAnimal, TerrestrialAnimal))
print(issubclass(Frog, TerrestrialAnimal))
# issubclass method

# isinstance class
print(isinstance(f, Frog))
print(isinstance(f, TerrestrialAnimal))
print(isinstance(f, AquaticAnimal))
print(isinstance(f, Animal))
print(isinstance(f, Dog))
print(isinstance(f, Puppy))
print(isinstance(p, Puppy))
print(isinstance(p, Dog))
print(isinstance(p, Animal))
#isinstance class


#Real Life example of method overriding

class Bank:
    def getroi(self):
        return 3

class SBI(Bank):
    def getroi(self):
        return 2.8

class ICICI(Bank):
    def getroi(self): #overriding
        return 3

class HDFC(Bank):
    def getroi(self): #overriding
        return 3.2

b = Bank()
print("Default ROI is: ", b.getroi())
s = SBI()
print("SBI ROI is: ", s.getroi())
i = ICICI()
print("ICICI ROI is: ", i.getroi())
h = HDFC()
print("HDFC ROI is: ", h.getroi())


#Data Abstraction in Python
# In Python we can acheive data abstraction by adding double_underscore
# In can not be accessed by object

class Person:
    __count = 0
    def __init__(self):
        Person.__count += 1

    def display(self):
        print("No of persons are: ", Person.__count)

p = Person()
p1 = Person()

try:
    print(p1.__count) # It will throw error as __count can not be extract outside the class
except Exception as e:
    print(e)
finally:
    p1.display()


# Abstraction
# it is a way to hide the internal working of a function from user
# user can know only the basic implemetation of a function, but won't be able to know the internal workings
# user can know what a function does, but can't know how it does
# Abstract class can be considered as blue print for other classed

# In Python, Abstraction can be achieved by using abstract classes and interfaces
# If a class contains, one or more abstract methods, then it is called as abstract class
# Abstract class can be inherited by other class, and the abstract methods can get their definition in other class

from abc import ABC, abstractmethod # python provides ABC class for abstraction
class Car(ABC): # abstract base class by inheriting ABC class

    @abstractmethod
    def gear(self): # it is an abstract method
        pass
    #An abstract class can contain both normal and abstract method
    def mileage(self): # it is a normal method (not abstract method)
        print("Default mileage is 15Kmph")

# in python, we need to use ABC class in order to make the base for defining a abstract base class
# to define abstract method, we need to use @abstractmethod decorator
# if a child class doesn;t implement the abstract method of the parent class,
# then it automatically becomes an abstract class

class Maruti(Car): # it becomes an abstract class, as it have not implemented the gear method(abstract method)
    def mileage(self):
        print("Mileage is 22 Kmph")

class Tesla(Car):
    def gear(self): #abstract method gets the definition here
        print("It has 6 gears")

class BMW(Car):
    def gear(self): #abstract method gets the definition here
        print("It has 5 gears")

t = Tesla()
t.gear()

b = BMW()
b.gear()

try:
    c = Car()
    #it will throw error,
    # as abstract class can't be instantiated, means we can't create object of abstract class
    c.mileage()
except Exception as e:
    print(e)

try:
    m = Maruti()
    #it will throw error,
    # as abstract class can't be instantiated, means we can't create object of abstract class
    m.mileage()
except Exception as e:
    print(e)






