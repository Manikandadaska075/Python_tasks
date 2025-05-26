Data Structures in Python
=

Python data structures are constructs that allow you to organize and store collections of data.

The primary built-in data structures are list, tuple, set, and dictionary.

### 1. List:
-----
Ordered, mutable sequences of items. They are versatile and commonly used for storing collections  of data that may need to be modified. Lists are defined by enclosing a comma-separated sequence of items within square brackets '[]'. These items can be of different data types, including numbers, strings, and even other lists.

```python
my_list = [1, "hello", 3.14, True]
```
 
<!-- ```python 
my_list = [1, 2, 3, 'apple', 'banana',2.4,-5.8]
my_list.append('orange')
``` -->

- Lists are ordered, meaning that the elements are stored in a specific sequence, and each element can be accessed by its index, starting from 0.

```python
print(my_list[0])  # Output: 1
print(my_list[1])  # Output: hello
```

- Lists are mutable, which means that their elements can be modified after the list is created. You can add, remove, or change elements using various list methods.

```python
my_list.append("world")  # Add an element to the end
my_list.insert(1, "new")  # Insert an element at a specific index
my_list.remove(3.14)  # Remove a specific element
my_list[0] = 10  # Change the value of an element
```

#### List Slicing: 

* Python list slicing is fundamental concept that let us easily access specific elements in a list.

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

* List comprehensions offer a concise way to create new lists based on existing iterables.

```python
squares = [x**2 for x in range(10)] #creates a list of squares from 0 to 9
```


+ Python provides a rich set of built-in functions for working with lists, such as len(), sort(), index(), and count().


|Method	        |Description                                                                    |
| -------       |-------------------                                                            |
|append()	    |Adds an element at the end of the list                                         |
|clear()	    |Removes all the elements from the list                                         |
|copy()	        |Returns a copy of the list                                                     |
|count()	    |Returns the number of elements with the specified value                        |
|extend()	    |Add the elements of a list (or any iterable), to the end of the current list   |
|index()	    |Returns the index of the first element with the specified value                |
|insert()	    |Adds an element at the specified position                                      |
|pop()	        |Removes the element at the specified position                                  |
|remove()	    |Removes the first item with the specified value                                |
|reverse()	    |Reverses the order of the list                                                 |
|sort()	        |Sorts the list                                                                 |


### 2. Tuples: 
----
Ordered, immutable sequences of items. They are similar to lists but cannot be modified after creation. Tuples are often used to represent fixed collections of data.

```python
empty_tuple = ()
my_tuple = (1, 2, 3, 'apple', 'banana')
```

Accessing Tuple Elements:
```python
my_tuple = (10, 20, 30)
print(my_tuple[0])  # Output: 10
print(my_tuple[2])  # Output: 30
```

```python
single_element_tuple = (5,)
```

```python
my_tuple = (1, 2, 2, 3, 4, 5)

print(len(my_tuple))  # Output: 6
print(max(my_tuple))  # Output: 5
print(min(my_tuple))  # Output: 1
print(sum(my_tuple))  # Output: 17
print(my_tuple.index(2))  # Output: 1
print(my_tuple.count(2))  # Output: 2
print(sorted(my_tuple))  # Output: [1, 2, 2, 3, 4, 5]

# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
print(tuple1 + tuple2)  # Output: (1, 2, 3, 4) 

# Repetition
print(tuple1 * 3)  # Output: (1, 2, 1, 2, 1, 2)

# Membership testing
print(3 in my_tuple)  # Output: True
print(6 not in my_tuple)  # Output: True
```

+ Alternatively, convert the tuple to a list, add the element(s) using list methods, and then convert back to a tuple. 
```python
original_tuple = (1, 2, 3)
temp_list = list(original_tuple)
temp_list.append(4)
new_tuple = tuple(temp_list)
print(new_tuple)  # Output: (1, 2, 3, 4)
```

Immutability
```python
my_tuple = (1, 2, 3)
my_tuple[0] = 10  # This will raise a TypeError

# Workaround:
my_list = list(my_tuple)
my_list[0] = 10
modified_tuple = tuple(my_list)  # Result: (10, 2, 3)
```
#### Use Cases:

Tuples are useful for storing data that should not be changed, such as coordinates, configuration settings, or records. They are also commonly used to return multiple values from a function.

### 3.Set
---
Unordered collections of unique items. Sets are useful for removing duplicates from a sequence and for performing set operations like union, intersection, and difference.

```python
my_set = {1, 2, 3, 'apple', 'banana'}
my_set.add('orange')
```

```python
list1=[1,2,3,4,4,5,5,6]
list1=set(list1)
print(list1)
```
+ To add an element to a set in Python, the add() method is used. This method adds a single element to the set. If the element is already present in the set, the set remains unchanged, as sets do not allow duplicate elements.

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
```

```python
my_set.add(2)  # Adding a duplicate element
print(my_set)  # Output: {1, 2, 3, 4}
```

+  To add multiple elements to a set at once, the update() method can be used. This method takes an iterable (like a list or another set) as an argument and adds all its elements to the set.

```python
my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

my_set.update([5, 7, 8])  # Adding some duplicate and some new elements
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
```
+ It's important to note that both add() and update() modify the set in place and do not return a new set.

Removes all the elements from the set:
  
```python
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits) # result set()
```

### 4. Dictionary
Collections of key-value pairs. Dictionaries are useful for storing and retrieving data based on a unique key.

```python
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(my_dict['name']) # result Alice
```

+ Use of value() method in dictionary
  
```python
dic={"one":1,"two":2,"three":3}
sum=0
for i in dic.values():
    sum+=i
print(sum)  # result 6
```

+ Use of key() method in dictionary
  
```python
dic={1:"one",2:"two",3:"three"}
if 4 in dic.keys():
    print(dic.get(4,"Yes"))
else:
    print(dic.get(4,"No"))
# result  No
```

+ item() method can assess both value and key
  
```python
dic={"a":1, "b":2,"c":3, "d":4}
dic1={j:i for i,j in dic.items() if j>=2} # comprehension
print(dic1)

dic={"a":1,"b":2,"c":3}
dic2={j:i for i,j in dic.items()} # comprehension
print(dic2)
```
+ Add item to the dictionary

```python 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
```
+ The pop() method removes the item with the specified key name:
```python 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
```





