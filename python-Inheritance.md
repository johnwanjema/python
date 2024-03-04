## Python Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

```bash
# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#Inherits the properties and methods from the Person class:
class Student(Person):
  pass

y = student('John','Wanjema')

x.printname()
```

## Add the __init__() Function

When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

```bash
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.

#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

```

## Super function
super() function that will make the child class inherit all the methods and properties from its parent:

```bash
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
  def printGradYear(self):
    print("My grad year is", self.graduationyear)

```

## Add  Properties

```bash
class Student(Person):
  def __init__(self, fname, lname,year):
    super().__init__(fname, lname)
    self.graduationyear = year

z =  Student('John','Doe',2024)
```