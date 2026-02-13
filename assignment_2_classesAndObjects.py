#Q1.) Basic Class and Object Creation
# Creating a class named Car
class Car:
    # Class attributes
    make = "Toyota"
    model = "Corolla"
    year = 2022

# Creating an object of Car
car1 = Car()

# Printing attributes
print(car1.make)
print(car1.model)
print(car1.year)
#-----------------------------------------
#Q2.) Methods in Class
class Car:
    def start_engine(self):
        print("Engine has started!")

car1 = Car()
car1.start_engine()
#-----------------------------------------
#Q3.) Class with Constructor
class Student:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Jack", 20)

print(student1.name)
print(student1.age)
#------------------------------------------
#Q4.) Class with Private Attributes
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def check_balance(self):
        return self.__balance

account = BankAccount("12345", 1000)

account.deposit(500)
account.withdraw(200)
print(account.check_balance())
#--------------------------------------------
#Q5.) Class Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

emp = Employee("John", 30, "E101")

print(emp.name)
print(emp.age)
print(emp.employee_id)
#---------------------------------------------
#Q6.) Method Overriding
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.employee_id}"

emp = Employee("John", 30, "E101")
print(emp)
#-----------------------------------------------
#Q7.) Class Composition
class Address:
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address  # Composition

addr = Address("MG Road", "Delhi", "110001")
person = Person("Jack", addr)

print(person.address.street)
print(person.address.city)
#------------------------------------------------
#Q8.) Class with Class Variables
class Counter:
    count = 0  # Class variable

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.get_count())
#--------------------------------------------------
#Q9.) Static Methods
import math

class MathOperations:
    @staticmethod
    def square_root(number):
        return math.sqrt(number)

print(MathOperations.square_root(16))
#--------------------------------------------------
#Q10.) Class with Properties
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

rect = Rectangle(10, 5)
print(rect.length)

rect.length = 20
print(rect.length)
#---------------------------------------------------
#Q11.) Abstract Base Class
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

c = Circle(5)
s = Square(4)

print(c.area())
print(s.area())
#----------------------------------------------------
#Q12.) Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2
print(v3.x, v3.y)
#----------------------------------------------------
#Q13.) Custom Exception
class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Not enough balance!")
        self.balance -= amount

account = BankAccount(1000)

try:
    account.withdraw(1500)
except InsufficientBalanceError as e:
    print(e)
#----------------------------------------------------
#Q14.) Context Manager
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Example usage
with FileManager("sample.txt", "w") as f:
    f.write("Hello World")
#-----------------------------------------------------
#Q15.) Method Chaining
class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, num):
        self.value += num
        return self

    def subtract(self, num):
        self.value -= num
        return self

    def multiply(self, num):
        self.value *= num
        return self

    def divide(self, num):
        self.value /= num
        return self

calc = Calculator()

result = calc.add(10).subtract(2).multiply(3).divide(4)
print(result.value)

