# Functions 
----

Python functions is a block of statements that return the specific task. The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.

Some Benefits of Using Functions:
+ Increase Code Readability 
+ Increase Code Reusability
  
Types of Functions in Python

+ Built-in library function: These are Standard functions in Python that are available to use.
+ User-defined function: We can create our own functions based on our requirements.

## Python Built in Functions

Function Name            |Description
---                      |---       
Python ascii()           |Returns a string containing a printable representation of an object
Python bin()             |Convert integer to a binary string
Python bool()            |Return or convert a value to a Boolean value i.e., True or False

## User-defined function

Creating and Call a functionin Python:

+ We can define a function in Python, using the def keyword. We can add any type of functionalities and properties to it as we require.

```python
def fun():
    print("hello")
fun()
def add(a,b):
    print(a+b)
add(1,3)
def fun2(a):
    return a+1
print(fun2(3))
myvalue=fun2(3)
print(myvalue)

"""
Result:
hello
4
4
4
"""
```

### Python Function with Parameters

Types of Python Function Arguments:
  -   Default argument
  -   Keyword arguments (named arguments)
  -   Positional arguments
  -   Arbitrary arguments (variable-length arguments *args and **kwargs)

1. Default arguments:
```python
def myhome(name,country="america"):
     print("my name is ",name)
     print("my country is ",country)
myhome("arun")

"""
Result
my name is  arun
my country is  america
"""
```

2. Keyword arguments:
```python
def myhome(name,num):
    print("my name is ",name)
    print("my number is ",num)
myhome(name="arun",num=3)

"""
Result:
my name is  arun
my number is  3
"""
```

3. Positional arguments:
```python
def myhome(name,country):
    print("my name is ",name)
    print("my country is ",country)
myhome("sam","India")

"""
Result:
my name is  sam
my country is  India
"""

```

- We used the Position argument during the function call so that the first argument (or value) is assigned to name and the second argument (or value) is assigned to age. By changing the position, or if you forget the order of the positions, the values can be used in the wrong places, as shown in the Case-2 example below, where 27 is assigned to the name and Suraj is assigned to the age.

```python
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

# You will get correct output because 
# argument is given in order
print("Case-1:")
nameAge("Suraj", 27)

# You will get incorrect output because
# argument is not in order
print("\nCase-2:")
nameAge(27, "Suraj")

"""
Results:
Case-1:
Hi, I am Suraj
My age is  27

Case-2:
Hi, I am 27
My age is  Suraj
"""
```

4. Arbitrary Keyword  Arguments

In Python Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:

- *args in Python (Non-Keyword Arguments)
- **kwargs in Python (Keyword Arguments)

Variable length non-keywords argument:
```python
def fun1(*kids):
    print("name:",kids[1])
fun1("sam","raju","akhil")

"""
Result:
name: raju
"""

```
Variable length keyword arguments:
```python
def fun2(**fruits):
    print("name:",fruits["fruits1"])
fun2(fruits1="banana",fruits2="orange",fruits3="apple")

"""
Result:
name: banana
"""

```

Only positional arguments:

```python
def fun3(x,y,/):
    print("addition output") 
fun3(1,2) # RESULT addition output
# fun3(x=1,y=3) #give error
```

Only keyword arguments:

```python
def fun4(*,a,b) :
    print("the subtract output")
fun4(a=2,b=5)  # result: the subtract output
# fun4(3,4) #give error
```

```python
def fun5(x,y,/,*,q,w): 
    print("data") 
fun5(1,2,q=5,w=6) # result: data
# fun5(X=1,y=2) #give error

def addsub(a,b,/,*,c,d):
    f=a+b
    print("Addition",f)
    e=0
    e=d-c
    print("Substration",e) 
addsub(2,2,c=5,d=10)

"""
result :
Addition 4
Substration 5
"""
```

Python Lambda:
+ A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.
  
```python
x=lambda a:a*2
print(x(2))
y=lambda a,b: a*b+1
print(y(2,3))

"""
Result:
4
7
"""
```

