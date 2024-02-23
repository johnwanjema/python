## Python Tuples
Tuples are written with round brackets.

```bash
thistuple = ("apple", "banana", "cherry")
print(thistuple)
```
Tuples are uchangeable, not item can be added or removed after it has been created.

Accessed using indexes starting from 0.

## Update Tuples
Workarounds to update a tuple.

1. convert it to list, change list, then convert back to tuple.

```bash
numbers = (1,2,3,4,)

list = list(numbers)

y[1]= 0

numbers = tuple(list)
```


2. Add a tuple to a tuple
```bash
numbers = (1,2,3,4,)

number = (5)

numbers += number
```

## Remove Items from a tuple
1. convert it to list, change list, then convert back to tuple.

The del tuple can be used to delete the tuple completely.

## Unpacking tuples

```bash
numbers = (1,2,4)

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
```
### Using asterisk *
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

```bash
numbers = (1,2,3,4,5,6)

(green, yellow, *red) = fruits

```

If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

## Python Tuples
Tuples are written with round brackets.

```bash
thistuple = ("apple", "banana", "cherry")
print(thistuple)
```
Tuples are uchangeable, not item can be added or removed after it has been created.

Accessed using indexes starting from 0.

## Update Tuples
Workarounds to update a tuple.

1. convert it to list, change list, then convert back to tuple.

```bash
numbers = (1,2,3,4,)

list = list(numbers)

y[1]= 0

numbers = tuple(list)
```


2. Add a tuple to a tuple
```bash
numbers = (1,2,3,4,)

number = (5)

numbers += number
```

## Remove Items from a tuple
1. convert it to list, change list, then convert back to tuple.

The del tuple can be used to delete the tuple completely.

## Unpacking tuples

```bash
numbers = (1,2,4)

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
```
### Using asterisk *
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

```bash
numbers = (1,2,3,4,5,6)

(green, yellow, *red) = fruits

```

If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

### Loop  through a tuple

```bash
for x in thistuple:
  print(x)

```

You can also loop through the tuple items by referring to their index number.
```bash

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
```

### Join Two Tuples
```bash

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

```

### Multiply Tuples

```bash

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

```