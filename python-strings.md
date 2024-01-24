## Python Strings

```bash
Text Type:	str
```

### Multiline Strings
You can assign a multiline string to a variable by using three quotes Or three single quotes:
```bash
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
```

### Strings are Arrays
Get the character at position 1 (remember that the first character has the position 0):
```bash
a = "Hello, World!"
print(a[1])
```
Loop through the letters in the word "banana":

```bash
for x in "banana":
  print(x)
```

### Strings length
```bash
a = "Hello, World!"
print(len(a))
```

### Check String
To check if a certain phrase or character is present in a string, we can use the keyword in.
```bash
txt = "The best things in life are free!"
print("free" in txt)
```

Print only if "free" is present:
```bash
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
```

Check if NOT

```bash
txt = "The best things in life are free!"
print("expensive" not in txt)
```

print only if "expensive" is NOT present:
```bash
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
```

## Slicing Strings
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

Get the characters from position 2 to position 5 (not included):
```bash
b = "Hello, World!"
print(b[2:5])

prints llo
```

Get the characters from the start to position 5 (not included):
```bash
b = "Hello, World!"
print(b[:5])
```

Get the characters from position 2, and all the way to the end:
```bash
b = "Hello, World!"
print(b[2:])
```

Use negative indexes to start the slice from the end of the string:
```bash
b = "Hello, World!"
print(b) 

prints orl
```
