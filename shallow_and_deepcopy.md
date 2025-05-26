### Shallow Copy:
A shallow copy creates a new object but doesn't create copies of the nested objects within the original. Instead, it inserts references to the original elements. Consequently, changes made to the nested objects in the copy will be reflected in the original, and vice versa.

Shallow copy only works for 1D lists of native data types.
Sublists, dicts and other objects will retain the sane reference to those objects.

```python
listA  = [2,4,6,[1,3]]
print(f"listA:",listA)
listB = list(listA)
listB[1] = 44
listB[3][0] = 55
print(f"listB:",listB)
print(f"listA:",listA)

"""
Output:
listA: [2, 4, 6, [1, 3]]
listB: [2, 44, 6, [55, 3]]
listA: [2, 4, 6, [55, 3]]
"""

```

### Deep Copy
A deep copy, on the other hand, creates a new object and recursively copies all nested objects present in the original. This results in two completely independent objects, where changes made to one do not affect the other.

```python
import copy
print("Deepcopy")
listA  = [2,4,6,[1,3]]
print(f"listA:",listA)
listB = copy.deepcopy(listA)
listB[1] = 44
listB[3][0] = 55
print(f"listB:",listB)
print(f"listA:",listA)

"""
output:
Deepcopy
listA: [2, 4, 6, [1, 3]]
listB: [2, 44, 6, [55, 3]]
listA: [2, 4, 6, [1, 3]]
"""
```

### comperhension

```python
syntax:

new_list = [expression for item in iterable if condition]
```

### Range

```python
syntax:

range(start, stop, step)
```

### for loop

```python
syntax:

for variable in sequence:
    # Code to be executed for each item
```

loop with string:

```python
for char in "Python":
    print(char)
"""
outputs:

P
y
t
h
o
n
"""
```

### while loop

syntax:

```python

while condition:
    # Code to be executed repeatedly
```

```python
count = 0
while count < 5:
    print("Count:", count)
    count += 1

"""
output:
Count: 0
Count: 1
Count: 2
Count: 3
Count: 4
"""

```

### Slicing:

List Slicing Syntax:

    list_name[start : end : step]

```python 
sub_list = my_list[1:3]  # Get a slice from index 1 to 2
```

```python
name="raghav"
name=name[:4:]
print(name) # result: ragh
```

```python
list2 = [0,1,2,3,4,5,6,7,8,9]
print(list2[::2]) # return 0,2,4,6,8
```

```python
list1=[1,2,3,4,5,6,7,8,9,10]
print(list1[-5:]) # result 6 7 8 9
```

```python
data="i was at home yesterday"
data2=data[-9: ]
print(data2)# result yesterday
```

```python
"""
Arithmetic Operators:

+ (Addition)
- (Subtraction)
* (Multiplication)
/ (Division)
% (Modulo - remainder of division)
// (Floor division - quotient without decimal part)
** (Exponentiation)


Assignment Operators:

= (Assign)
+= (Add and assign)
-= (Subtract and assign)
*= (Multiply and assign)
/= (Divide and assign)
%= (Modulo and assign)
//= (Floor divide and assign)
**= (Exponentiate and assign)
&= (Bitwise AND and assign)
|= (Bitwise OR and assign)
^= (Bitwise XOR and assign)
>>= (Right shift and assign)
<<= (Left shift and assign)


Comparison Operators:

== (Equal to)
!= (Not equal to)
> (Greater than)
< (Less than)
>= (Greater than or equal to)
<= (Less than or equal to)


Logical Operators:

and (Logical AND)
or (Logical OR)
not (Logical NOT)


Bitwise Operators:

& (Bitwise AND)
| (Bitwise OR)
^ (Bitwise XOR)
~ (Bitwise NOT)
<< (Left shift)
>> (Right shift)


Membership Operators:

Used to test if a sequence is present in an object.

in (Returns True if a sequence is found in the specified object)
not in (Returns True if a sequence is not found in the specified object)

Identity Operators:

Used to compare the memory locations of two objects.
is (Returns True if both variables are the same object)
is not (Returns True if both variables are not the same object)

"""
```

### Type casting:

Two type:

+ Implicit type casting: 
  
  Python automatically converts one data type to another. This usually happens when performing operations between different data types. For example, when adding an integer and a float, Python will implicitly convert the integer to a float before performing the addition.

```python

    x = 10
    y = 2.5
    z = x + y  # x is implicitly converted to float
    print(z)  # Output: 12.5
    print(type(z)) # Output: <class 'float'>
```

+ Explicit type casting: 
  
  The programmer manually converts a data type using built-in functions like int(), float(), str(), bool(), etc. 

```python

    a = "123"
    b = int(a)  # a is explicitly converted to integer
    print(b)  # Output: 123
    print(type(b)) # Output: <class 'int'>
    
    c = 3.14
    d = str(c) # c is explicitly converted to string
    print(d) # Output: 3.14
    print(type(d)) # Output: <class 'str'>

```

### If-Else

```python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

"""
Output:
a is greater than b
"""
```