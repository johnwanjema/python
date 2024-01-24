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