class Employee:
    count = 0 # class variable. It is exchanged by all the instances

    def __init__(self, emp_id, bu):
        self.emp_id = emp_id # instance variable
        self.bu = bu
        Employee.count+=1 # accessing the class variable using class name

    def display(self): #method is a function associated with an object
        print("Hi", self.emp_id, self.bu)


e1 = Employee(429877, 'FSDC') #an instance of the class
e1.display() #method is associated with e1 object

e2 = Employee(429878, 'ASDC') #an instance of the class
e2.display() #method is associated with e2 object

print(Employee.count) #class variable

