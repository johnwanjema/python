## Python loops

### IF loop
```bash
# if
if b > a:
  print("b is greater than a")

# elif
if b > a:
  print("b is greater than a")
elif:
  print("a is greater than b")

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# short hand if
if a > b: print("a is greater than b")

Short Hand If ... Else
print("A") if a > b else print("B")

```

### While loop

```bash
while i < 6:
  print(i)
  i += 1
```
Break statement we can stop the loop even if the while condition is true.

```bash
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
```
continue statement we can stop the current iteration, and continue with the next

```bash
## wont print 3
i = 1
while i < 6:
   i += 1
  if i == 3:
    continue
  print(i)
```

### For loop
```bash
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

```

Break statement we can stop the loop before it has looped through all the items:

```bash
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

```

Continue statement we can stop the current iteration of the loop, and continue with the next:

```bash
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

```

The range function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number

```bash
# from 0 to 5
for x in range(6):
  print(x)

# from 2 to 5 does not include 6
for x in range(2, 6):
  print(x)

# specify increment value. Increment by 3 from 3 to 29
for x in range(2, 30, 3):
  print(x)
```