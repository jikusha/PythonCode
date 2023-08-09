#class variable
# instance variable

# class variable are shared by all the instances
# class or static variables are defined outside of any method
# instance variable are unique for each objects
# Instance variables are assigned within a constructor or other methods
# class variables are defined insided the class


class Dog:
    animal = 'Dog' #class variable

    def __init__(self, breed):
        self.breed = breed #instance variable

    def setColor(self, color):
        self.color = color #instance variable

    def display(self):
        print(f"This dog is of type {self.breed} and color {self.color}")

d = Dog("LCCian")
d.setColor("brown")
d.display()
print(d.animal)
print(Dog.animal) #class variables can be accessed by class name also



# constructors
# it is used to initiallized the data members of the class at the time of object creation
# default constructor = It doesn't take any arguments except self
# parameterized constructor = it takes arguments
# constructor overloading is  not possible

class Car:
    def __init__(self, name=None):
        if name is None:
            print("Default constructor")
        else:
            self.name = name
            print("Parameterized constructor")

    def display(self):
        if not hasattr(self, 'name'):
            print("there are no parameters")
        else:
            print(f"Name of car is: {self.name}")

c1 = Car()
c1.display()

c2 = Car("Tesla")
c2.display()



# destructors
# __del__() method is destructor in python
# it is getting called, when an object is deleted or when the program ends
# python has a garbage collector which manages memory management automatically, so in python desctructor is no as much needed
# like in C++

# useful for automatic clean up


class Employee:
    def __init__(self):
        print("Constructor is called")

    def __del__(self): # it will be called when a program ends, or we are deleting the object reference
        print("Destructor is called")


e = Employee()
del e


# inheritance

class Person:
    def __init__(self, name, add):
        self.name = name
        self.address = add
        self.age = 24
        self.__password = 'ABC' # private member
        print("Parent constructor is getting invoked")

    def display(self):
        print(f"name = {self.name}, address = {self.address}")

    def work(self):
        print(f"{self.name} works as a Person")

    def displayPrivate(self):
        print(f"pass word is : {self.__password}")

class Student:
    def __init__(self):
        print("Student constructor is getting invoked")

class Emp(Person):
    def __init__(self, name, add, emp_id, company):
        super().__init__(name, add)
        self.emp_id = emp_id
        self.company = company
        print("Child constructor is getting invoked")

    def display(self):
        print(f"name = {self.name}, address = {self.address}, emp_id = {self.emp_id}, company = {self.company}")

    def displayPrivate(self):
        print(f"pass word is : {self.__password}") # won't be able to access private members of parent class
        # hence private members can;t be inherited

e1 = Emp("Jiku", "bangalore", "429877", "CGI")
e1.display()
e1.work()
try:
    e1.displayPrivate()
except Exception as e:
    print(e)

print(f"Age is: {e1.age}")

p = Person("dfd", "sdsd")
p.displayPrivate()


class A(Student, Person): # multiple inheritance
    def __init__(self):
        super().__init__() # super() will always calls the constructor of the class, which is mentioned first
        Student.__init__(self) # student constructor (if we don't use super(), then we need to send self explicitly)
        Person.__init__(self, "Jiku", "GHY") # Person constructor

a = A()


# In Python Object class is the parent class of all the classes




# Encapsulation
# It is the concept of binding methods and attributes together that work on data
# with the help of class we can achieve Encapsulation
# this puts restriction on accessing the attributes and methods directly
# they can be accessed by object of the class
# it has a concept of private member
# private members can not be accessed outside the class, can be accessed by method of that class only



# protected members
# need to be prefixed by _

class CSStudent:
    stream = 'CSE' # static or class variable # it gets memory before object creation
    def __init__(self, name):
        self.name = name # instance variable # it gets memory during object creation

s1 = CSStudent("Jiku")
s2 = CSStudent("Biki")
print(s1.name)
print(s2.name)
print(s1.stream) # can be accessed by object
print(s2.stream) # can be accessed by object
print(CSStudent.stream) # can be accessed by class name

s1.stream = 'EE' # it will change only for s1 object
print(s1.stream)
print(s2.stream)
print(CSStudent.stream)

CSStudent.stream = 'EE' # it will change for all
print(s1.stream)
print(s2.stream)
print(CSStudent.stream)

# advantages of static or class variable
# memory efficiency => as all the objects share the same thing, no there are no need to create multiple copies for all objects



# class methods vs static methods

# class method is bound to class, not to object

# with the help of class method, we can change the state of the class

# it can access class variables and can modify it

class Employee:
    company = 'Amazon'
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name = {self.name}, company = {self.company}")

    @classmethod
    def changeCompany(cls, new_company): # it will receive the first parameter as reference to class, not to object
        cls.company = new_company


e1 = Employee("Jiku")
e1.changeCompany("CGI")
e1.show()
print(Employee.company)
Employee.changeCompany("Google")
print(Employee.company)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def createStudent(cls, inp): # alternative of constructor
        return cls(inp.split('-')[0], int(inp.split('-')[1]))

s1 = Student("Jiku", 24)
print(s1.name)
print(s1.age)

inp = "Biki-25"
s2 =Student(inp.split('-')[0], inp.split('-')[1])
print(s2.name)
print(s2.age)

s3 = Student.createStudent("Bankim-26")
print(s3.name)
print(s3.age)


# static methods
# these are utility type methods
# neither belongs to class, nor to objects
# they know nothing about the class state
# we define it withing the class, so that it will be associated with the class and other take get the benefit of this method

class Math:
    @staticmethod
    def add(a,b): # no need of self parameter
        print(a+b)

Math.add(4,5) # for calling static method, no need to create object

m = Math()
m.add(6,7)
