# -------------------- Question 1: Single Inheritance Basic --------------------

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

dog1 = Dog("Buddy", "Canine", "Labrador")
print("Question 1 Output:", dog1.name, dog1.species, dog1.breed)


# -------------------- Question 2: Method Overriding in Single Inheritance --------------------

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a {self.breed} {self.species}"

dog2 = Dog("Max", "Canine", "Beagle")
print("Question 2 Output:", dog2)


# -------------------- Question 3: Single Inheritance with Additional Methods --------------------

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def bark(self):
        print("Woof! Woof!")

dog3 = Dog("Rocky", "Canine", "Pug")
print("Question 3 Output:")
dog3.bark()


# -------------------- Question 4: Multiple Inheritance Basic --------------------

class Walker:
    def walk(self):
        print("Walking...")

class Runner:
    def run(self):
        print("Running...")

class Athlete(Walker, Runner):
    pass

athlete1 = Athlete()
print("Question 4 Output:")
athlete1.walk()
athlete1.run()


# -------------------- Question 5: Method Resolution Order (MRO) --------------------

class Athlete(Walker, Runner):
    def walk(self):
        print("Athlete walking...")
        super().walk()

athlete2 = Athlete()
print("Question 5 Output:")
athlete2.walk()


# -------------------- Question 6: Multiple Inheritance with Additional Attributes --------------------

class Athlete(Walker, Runner):
    def __init__(self, training_hours):
        self.training_hours = training_hours

    def train(self):
        print("Training Hours:", self.training_hours)

athlete3 = Athlete(5)
print("Question 6 Output:")
athlete3.train()


# -------------------- Question 7: Diamond Problem in Multiple Inheritance --------------------

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

d1 = D()
print("Question 7 Output:")
d1.show()
print("MRO:", D.__mro__)


# -------------------- Question 8: Using super() in Single Inheritance --------------------

class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

circle1 = Circle("Red", 10)
print("Question 8 Output:", circle1.color, circle1.radius)


# -------------------- Question 9: Using super() in Multiple Inheritance --------------------

class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id

class Manager(Person, Employee):
    def __init__(self, name, employee_id):
        Person.__init__(self, name)
        Employee.__init__(self, employee_id)

manager1 = Manager("Alice", 101)
print("Question 9 Output:", manager1.name, manager1.employee_id)


# -------------------- Question 10: Method Overriding and super() --------------------

class Vehicle:
    def start(self):
        print("Vehicle starting...")

class Car(Vehicle):
    def start(self):
        print("Car starting...")
        super().start()

car1 = Car()
print("Question 10 Output:")
car1.start()


# -------------------- Question 11: Multiple Inheritance with Different Methods --------------------

class Flyer:
    def fly(self):
        print("Flying...")

class Swimmer:
    def swim(self):
        print("Swimming...")

class Superhero(Flyer, Swimmer):
    pass

hero = Superhero()
print("Question 11 Output:")
hero.fly()
hero.swim()


# -------------------- Question 12: Complex Multiple Inheritance --------------------

class Base1:
    def __init__(self, a):
        self.a = a

class Base2:
    def __init__(self, b):
        self.b = b

class Derived(Base1, Base2):
    def __init__(self, a, b, c):
        Base1.__init__(self, a)
        Base2.__init__(self, b)
        self.c = c

derived1 = Derived(1, 2, 3)
print("Question 12 Output:", derived1.a, derived1.b, derived1.c)


# -------------------- Question 13: Checking Instance Types --------------------

class Animal:
    pass

class Cat(Animal):
    pass

animal1 = Animal()
cat1 = Cat()

print("Question 13 Output:")
print(isinstance(animal1, Animal))
print(isinstance(cat1, Animal))
print(isinstance(cat1, Cat))


# -------------------- Question 14: Polymorphism with Inheritance --------------------

class Bird:
    def speak(self):
        print("Bird sound")

class Parrot(Bird):
    def speak(self):
        print("Parrot says Hello")

class Penguin(Bird):
    def speak(self):
        print("Penguin makes sound")

birds = [Parrot(), Penguin()]

print("Question 14 Output:")
for bird in birds:
    bird.speak()


# -------------------- Question 15: Combining Single and Multiple Inheritance --------------------

class Device:
    def __init__(self, brand):
        self.brand = brand

class Phone(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

class Camera:
    def __init__(self, resolution):
        self.resolution = resolution

class Smartphone(Phone, Camera):
    def __init__(self, brand, model, resolution):
        Phone.__init__(self, brand, model)
        Camera.__init__(self, resolution)

smartphone1 = Smartphone("Apple", "iPhone 15", "48MP")
print("Question 15 Output:", smartphone1.brand, smartphone1.model, smartphone1.resolution)
