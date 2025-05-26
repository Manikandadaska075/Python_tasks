## OOPs Concepts in Python

Class in Python
Objects in Python
Polymorphism in Python
Encapsulation in Python
Inheritance in Python

### Class:

+ A class in Python is a user-defined template for creating objects. It bundles data and functions together, making it easier to manage and use them. When we create a new class, we define a new type of object. We can then create multiple instances of this object type.

+ Classes are created using class keyword. Attributes are variables defined inside the class and represent the properties of the class. Attributes can be accessed using the dot . operator (e.g., MyClass.my_attribute).

### Create a Class:

```python
# define a class
class Dog:
    sound = "bark"  # class attribute
```

### Create Object:
+ An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data.

Create an object from Dog class.

```python
class Dog:
    sound = "bark" 

# Create an object from the class
dog1 = Dog()

# Access the class attribute
print(dog1.sound)
```
sound attribute is a class attribute. It is shared across all instances of Dog class, so can be directly accessed through instance dog1.

### Using __init__() Function:

+ In Python, class has __init__() function. It automatically initializes object attributes when an object is created.

```python
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

```

class Dog: Defines a class named Dog.
species: A class attribute shared by all instances of the class.

__init__ method: Initializes the name and age attributes when a new object is created.

### Initiate Object with __init__:

```python
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name)  # Output: Buddy
print(dog1.species)  # Output: Canine

"""
Result:

Buddy
Canine
"""
```

dog1 = Dog("Buddy", 3): Creates an object of the Dog class with name as "Buddy" and age as 3.

dog1.name: Accesses the instance attribute name of the dog1 object.

dog1.species: Accesses the class attribute species of the dog1 object.

### Self Parameter
+ Self parameter is a reference to the current instance of the class. It allows us to access the attributes and methods of the object.

```python
class Dog:
    def __init__(self, name, age):  
        self.name = name 
        self.age = age

    def bark(self): 
        print(f"{self.name} is barking!")

# Creating an instance of Dog
dog1 = Dog("Buddy", 3)
dog1.bark()

"""
Result:

Buddy is barking!
"""
```

Inside bark(), self.name accesses the specific dog's name and prints it.

When we call dog1.bark(), Python automatically passes dog1 as self, allowing access to its attributes.

### __str__ Method:
+ __str__ method in Python allows us to define a custom string representation of an object. By default, when we print an object or convert it to a string using str(), Python uses the default implementation, which returns a string like <__main__.ClassName object at 0x00000123>.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."  # Correct: Returning a string
      
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1)  
print(dog2)

"""
Result:

Buddy is 3 years old.
Charlie is 5 years old.
"""
```

__str__ Implementation: Defined as a method in the Dog class. Uses the self parameter to access the instance's attributes (name and age).

Readable Output: When print(dog1) is called, Python automatically uses the __str__ method to get a string representation of the object. Without __str__, calling print(dog1) would produce something like <__main__.Dog object at 0x00000123>.

Class Variables:
- These are the variables that are shared across all instances of a class. It is defined at the class level, outside any methods. All objects of the class share the same value for a class variable unless explicitly overridden in an object.

Instance Variables:
- Variables that are unique to each instance (object) of a class. These are defined within __init__ method or other instance methods. Each object maintains its own copy of instance variables, independent of other objects.

```python
class Dog:
    # Class variable
    species = "Canine"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)     # (Instance variable)

# Modify instance variables
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)

"""
Result:

Canine
Buddy
Charlie
Max
Feline
Feline
"""
```

Class Variable (species): Shared by all instances of the class. Changing Dog.species affects all objects, as it's a property of the class itself.

Instance Variables (name, age): Defined in the __init__ method. Unique to each instance (e.g., dog1.name and dog2.name are different).

Accessing Variables: Class variables can be accessed via the class name (Dog.species) or an object (dog1.species). Instance variables are accessed via the object (dog1.name).

Updating Variables: Changing Dog.species affects all instances. Changing dog1.name only affects dog1 and does not impact dog2.

### Polymorphism:

+ In OOP, polymorphism allows methods in different classes to share the same name but perform distinct tasks. This is achieved through inheritance and interface design. Polymorphism complements other OOP principles like inheritance (sharing behavior) and encapsulation (hiding complexity) to create robust and modular applications.

```python
class Shape:
    def area(self):
        return "Undefined"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(2, 3), Circle(5)]
for shape in shapes:
    print(f"Area: {shape.area()}")

```

+ The code showcases polymorphism using a parent class Shape and child classes Rectangle and Circle.
Parent Class Shape: Contains a generic area method returning "Undefined", acting as a placeholder for derived classes to override.
+ Child Class Rectangle: Initializes length and width via the __init__ constructor. Overrides the area method to return the rectangle's area as length * width.
+ Child Class Circle: Initializes radius via the __init__ constructor. Overrides the area method to return the circle's area as 3.14 * radius^2.
+ Polymorphic Behavior: A list of shape objects (Rectangle and Circle) is created. A for loop iterates through the list, calling the area method on each object. The method executed is determined by the object's type, showcasing polymorphism.

#### Types of Polymorphism:

Compile-time Polymorphism:

Found in statically typed languages like Java or C++, where the behavior of a function or operator is resolved during the program's compilation phase.

Examples include method overloading and operator overloading, where multiple functions or operators can share the same name but perform different tasks based on the context.

In Python, which is dynamically typed, compile-time polymorphism is not natively supported. Instead, Python uses techniques like dynamic typing and duck typing to achieve similar flexibility.

Runtime Polymorphism:

Occurs when the behavior of a method is determined at runtime based on the type of the object.

In Python, this is achieved through method overriding: a child class can redefine a method from its parent class to provide its own specific implementation.

Python's dynamic nature allows it to excel at runtime polymorphism, enabling flexible and adaptable code.

```python
class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())  # Calls the overridden method based on the object type

"""
output:
 
Bark
Meow
Some generic sound
```

Here, the sound method behaves differently depending on whether the object is a Dog, Cat or Animal and this decision happens at runtime. This dynamic nature makes Python particularly powerful for runtime polymorphism.

Inheritance Class Polymorphism:

Inheritance-based polymorphism occurs when a subclass overrides a method from its parent class, providing a specific implementation. This process of re-implementing a method in the child class is known as Method Overriding.  

```python
class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow
```

Class Animal: Acts as the base (parent) class. Contains a method sound that provides a default behavior, returning "Some generic animal sound". This serves as a generic representation of the sound method for all animals.

Class Dog: Inherits from the Animal class (denoted by class Dog(Animal)). Overrides the sound method to return "Woof Woof!", a behavior specific to dogs. This demonstrates method overriding, where the subclass modifies the implementation of the parent class’s method.

Class Cat: Inherits from the Animal class (denoted by class Cat(Animal)). Overrides the sound method to return "Meow", a behavior specific to cats. Like Dog, this also demonstrates method overriding.

### Inheritance in Python:

Inheritance is an object-oriented programming (OOP) feature that allows a class (called a child or subclass) to inherit attributes and methods from another class (called a parent or superclass). It promotes code reusability.

Types of Inheritance in Python:

+ Single Inheritance

+ Multiple Inheritance

+ Multilevel Inheritance

+ Hierarchical Inheritance

+ Hybrid Inheritance

Single Inheritance:   
One child class inherits from one parent class.
```python
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()
```

Multiple Inheritance:

A child class inherits from multiple parent classes.
```python
class Father:
    def skills(self):
        print("Father: Gardening")

class Mother:
    def skills(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def own_skill(self):
        print("Child: Painting")

c = Child()
c.skills()  # Python uses Method Resolution Order (MRO) – it will call Father's skills
c.own_skill()
```

Multilevel Inheritance:

A child class inherits from a class, which in turn inherits from another class.
```python
class Grandparent:
    def house(self):
        print("Grandparent's house")

class Parent(Grandparent):
    def car(self):
        print("Parent's car")

class Child(Parent):
    def bike(self):
        print("Child's bike")

c = Child()
c.house()
c.car()
c.bike()
```

Hierarchical Inheritance:

Multiple child classes inherit from one parent class.
```python
class Parent:
    def speak(self):
        print("Parent speaks")

class Child1(Parent):
    def play(self):
        print("Child1 plays")

class Child2(Parent):
    def study(self):
        print("Child2 studies")

c1 = Child1()
c2 = Child2()
c1.speak()
c2.speak()
```

Hybrid Inheritance:

Combination of multiple types of inheritance.

```python
class A:
    def method_A(self):
        print("A method")

class B(A):
    def method_B(self):
        print("B method")

class C(A):
    def method_C(self):
        print("C method")

class D(B, C):
    def method_D(self):
        print("D method")

d = D()
d.method_A()
d.method_B()
d.method_C()
d.method_D()
```

### Abstraction:

+ Abstraction in Object-Oriented Programming (OOP) using Python is a principle that allows you to hide the internal implementation details of a class and expose only the necessary functionalities. It helps in reducing complexity and increases efficiency by showing only essential features of an object.

Key Concepts of Abstraction in Python:

Abstract Class: A class that cannot be instantiated directly. It often contains one or more abstract methods.

Abstract Method: A method that is declared but contains no implementation. Subclasses must implement these methods.

Python provides the abc module (Abstract Base Classes) to implement abstraction.

from abc import ABC, abstractmethod
```python
# Abstract class
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass  # Abstract method with no implementation

    def sleep(self):
        print("Sleeping...")  # Concrete method

# Subclass that implements the abstract method
class Dog(Animal):
    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Usage
dog = Dog()
dog.make_sound()  # Output: Bark!
dog.sleep()       # Output: Sleeping...

cat = Cat()
cat.make_sound()  # Output: Meow!
```

Benefits of Abstraction

Hides complex code from the user.

Focuses on what an object does instead of how.

Supports the design of more scalable and maintainable code.

### Polymorphism in Python:

Polymorphism means "many forms." In Python, it allows the same interface (method or function) to behave differently based on the object calling it.

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Polymorphism in action
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())  # Output will be Woof! then Meow!

```

The speak() method works differently depending on the object's class.
 
### super() in Python:

The super() function is used to call a method from a parent (superclass) in a child (subclass). It's especially useful in inheritance to avoid hardcoding parent class names and support multiple inheritance cleanly.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calls the __init__ of Animal
        self.breed = breed

    def speak(self):
        return f"{self.name} barks."

dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())          # Buddy barks.
print(dog.name, dog.breed)  # Buddy Golden Retriever
```

super().__init__(name) initializes the name attribute from the parent class.