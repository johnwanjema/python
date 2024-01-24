## Python Variables
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

```bash
x = 5
y = "John"
print(x)
print(y)
```

Variables do not need to be declared with any particular type, and can even change type after they have been set.
```bash
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
```

### Casting
If you want to specify the data type of a variable, this can be done with casting.
```bash
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```

### Get the Type
If you want to specify the data type of a variable, this can be done with casting.
```bash
x = 5
y = "John"
print(type(x))
print(type(y))
```

### Multi Words Variable Names
Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:

#### Camel Case
```bash
myVariableName = "John"
```
#### Pascal Case
```bash
MyVariableName = "John"
```

#### Snake Case
```bash
my_variable_name = "John"
```

### Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:
```bash
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```

### One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:

```bash
x = y = z = "Orange"
print(x)
print(y)
print(z)
```

### Unpack a Collection
Unpack a list:

```bash
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
```


### The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

Also, use the global keyword if you want to change a global variable inside a function.

```bash
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```
