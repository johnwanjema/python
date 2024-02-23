## Python Sets

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

When we say that dictionaries are ordered (python 3.7), it means that the items have a defined order, and that order will not change.

Dictionaries cannot have two items with the same key. Duplicate values will overwrite existing values:

The values in dictionary items can be of any data type:

```bash
userDict = {
  "first_name": "John",
  "last_name": "Wanjem",
}

# loop dict
for x in userDict:
  print(x)

# You can also use the values() method 
for x in userDict.values():
  print(x)
  
# Acess items
print(userDict["first_name"])

x = userDict.get("first_name")

# prints dict length
print(len(userDict))

# Get Keys - returns a list of all the keys in the dictionary

x = userDict.keys()

# Get values - return a list of all the values in the dictionary.

x = userDict.values()

```


## dict constructor

```bash
userDict = dict(name = "John", age = 36, country = "Kenya")
print(userDict)

# prints set length
print(len(myfruits))
```

## Get Items

The items() method will return each item in a dictionary, as tuples in a list.

```bash
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)


dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

```

## Check if Key exists
```bash

if "first_name" in userDict:
  print("exists")

```

## Remove Items

The pop() method removes the item with the specified key name.
```bash
userDict.pop("first_name")
```

The popitem() method removes the last inserted item.
```bash
userDict.popitem()
```

The del keyword removes the item with the specified key name. It can also be used to delete the dictionary completely.

```bash
del userDict["first_name"]

del userDict
```

Clear method empties the dictionary:

```bash

userDict.clear()
```


