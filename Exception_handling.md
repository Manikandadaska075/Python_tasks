The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

## Exception Handling:

When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the try statement:

```python
try:
  print(x)
except:
  print("An exception occurred")

"""
output:
An exception occurred
"""

```
## Else:
You can use the else keyword to define a block of code to be executed if no errors were raised:

```python
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

"""
output:

Hello
Nothing went wrong
"""
```

## Finally:
The finally block, if specified, will be executed regardless if the try block raises an error or not.

```python
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

"""
Output

Something went wrong
The 'try except' is finished
"""
```

## File Exception:
```python
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

"""
Output:
Something went wrong when writing to the file
"""
```

## Raise an exception:
As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the raise keyword.

The raise keyword is used to raise an exception.

```python
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

"""
Output:
Exception: Sorry, no numbers below zero
"""

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

"""
Output:
TypeError: Only integers are allowed
"""
```

# Built-in Exceptions

## ArithmeticError Exception:

### ZeroDivisionError:

A ZeroDivisionError occurs if you try to divide a number with 0.

A ZeroDivisionError is a type of ArithmeticError.

Handling the ZeroDivisionError in a try...except statement:

```python
try:
  print(10 / 0)
except ZeroDivisionError:
  print("Error in calculation")
except:
  print("Something else went wrong")

"""
Output:
Error in calculation
"""
```

### OverflowError Exception:

Handling the OverflowError in a try...except statement:
```python
import math
try:
  print(math.exp(999))
except OverflowError:
  print("The number is too high")
except:
  print("Something else went wrong")

"""
Output:
The number is too high
"""
```

## AssertionError Exception:

Error in assert statement

The AssertionError exception occurs when an assert statement fails.

```python
x = "hello"
try:
  assert x == "goodbye"
except AssertionError:
  print("Error in assert statement")
except:
  print("Something else went wrong")

"""
Output:
Error in assert statement
"""
```

## AttributeError Exception:
The AttributeError exception occurs when you try to execute a property or method that does not exist on the current object.

```python
x = "Hello"
try:
  print(x.toUpperCase())
except AttributeError:
 print("Oops! Strings do not have a toUpperCase method!")
except:
 print("Something else went wrong")

"""
Output:
Oops! Strings do not have a toUpperCase method!
"""
```

## ImportError:

Raised when an imported module does not exist

## IndentationError Exception:

The IndentationError exception occurs when indentitation is missing, or is wrong.

You have to use the same number of spaces in the same block of code, otherwise you get an IndentationError.

```python

if 5 > 2:
  print("Five is greater than two!")
   print("Makes sence!")
"""
Output:
print("Makes sence!")
IndentationError: unexpected inden
"""
```

## IndexError Exception:

A IndexError occurs if you try access a list item with an index that does not exist:

```python
x = ["apple", "banana", "cherry"]
try:
  print(x[5])
except IndexError:
  print("You are trying to access an item that does not exist!")
except:
  print("Something else went wrong")

"""
Output:
You are trying to access a item that does not exist!
"""

```

## KeyError Exception:

The KeyError exception occurs when you use a key on a dictionary, and the key does not exist.

```python
fruit = {"name": "apple", "color": "red"}
try:
  print(fruit["price"])
except KeyError:
  print("You are trying to access a dictionary item that does not exist!")
except:
  print("Something else went wrong")

"""
Output:
You are trying to access a dictionary item that does not exist!
"""
```

## NameError Exception:

The NameError exception occurs if you use a variable that is not defined.

```python

try:
  print(x)
except NameError:
 print("Variable x is not defined")
except:
 print("Something else went wrong")

"""
Output:
Variable x is not defined
"""
```

## TypeError Exception:

A TypeError occurs if you try to concatenate a string and a number:

```python
try:
  x = "hello" + 15
except TypeError:
  print("Please convert to string before concatenate")
except:
  print("Something else went wrong")

"""
Output
Please convert to string before concatenate
"""
```

## ValueError Exception:

A ValueError occurs if you send a string into a function that requires a number:

```python
try:
  x = float("hello")
except ValueError:
  print("The value has wrong format")
except:
  print("Something else went wrong")

"""
Output:
The value has wrong format
"""
```

# User-Defined Exception

Creating User-Defined Exceptions:

Inheritance:

User-defined exceptions are created by defining a new class that inherits from the base Exception class or one of its subclasses.

Class Definition:

The new class typically includes a constructor (__init__) to initialize the exception with a custom error message.

```python
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    raise CustomError("This is a custom error message.")
except CustomError as e:
    print(f"Caught an exception: {e}")

"""
Output:
Caught an exception: This is a custom error message.
"""
```
raise Keyword:

The raise keyword is used to trigger the user-defined exception, followed by an instance of the custom exception class.


# Scope in python

A variable is only available from inside the region it is created. This is called scope.

### local scope:

A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

```python
def myfunc(x):
  x = 5+x
  print(x)
x= 10
myfunc(x)
print(x)

"""
Output:
15
10
"""
```

### Global Scope:

A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local.

```python
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

"""
Output:
300
300
"""
```

#### Naming Variables:

If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):

```python
x = 300

def myfunc():
  x = 200
  print(x)
myfunc()
print(x)

"""
Output:
200
300
"""
```

#### Global Keyword

If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

The global keyword makes the variable global.

If you use the global keyword, the variable belongs to the global scope:

```python
def myfunc():
  global x
  x = 300
myfunc()
print(x)

"""
Output:
300
"""
```

Also, use the global keyword if you want to make a change to a global variable inside a function.

```python
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)

"""
Output:
200
"""
```

#### Nonlocal Keyword

The nonlocal keyword is used to work with variables inside nested functions.

The nonlocal keyword makes the variable belong to the outer function.

```python
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

"""
Output
hello
"""
```

# Decorators in Python

In Python, decorators are a powerful and flexible way to modify or extend the behavior of functions or methods, without changing their actual code. A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality.

Decorators are often used in scenarios such as logging, authentication and memorization, allowing us to add additional functionality to existing functions or methods in a clean, reusable way.

```python
# A simple decorator function
def decorator(func):
  
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

# Applying the decorator to a function
@decorator

def greet():
    print("Hello, World!")

greet()

"""
Output:
Before calling the function.
Hello, World!
After calling the function.
"""
```

Explanation:

Decorator takes the greet function as an argument.
It returns a new function (wrapper) that first prints a message, calls greet() and then prints another message.
The @decorator syntax is a shorthand for greet = decorator(greet).