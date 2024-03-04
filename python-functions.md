## Python functions

A function is a block of code which only runs when it is called.

```bash
def function_name():
  print('function call')

function_name()
```
Arguments - Information can be passed into functions as arguments.

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.

```bash
def function_name(date,month,year):
  print("The date is " + date + month + year)

function_name()
```
Arbitrary Arguments, *args

```bash
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
```
Default Parameter Value

```bash
def my_function(country = "Kenya"):
  print("I am from " + country)
  
```

Arbitrary Keyword Arguments, **kwargs

If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

```bash
def my_function(**kid):
  print("My last name is " + kid["lname"])

my_function(fname = "John", lname = "Wanjema")
```

## lambda functions
lambda function is a small anonymous function.

Add 5 to argument a, and return the result:
```bash
x = lambda a : a + 5

print(x(5))

Multiply argument a with argument b and return the result:
x = lambda a, b, c : a * b * c
```