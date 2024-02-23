## Python Sets

Sets are used to store multiple items in a single variable.

A set is a collection which is unordered, unchangeable*, and unindexed.

*Set items are unchangeable, but you can remove items and add new items.

Unordered means that the items in a set do not have a defined order.

Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Sets cannot have two items with the same value. Duplicate values are ignored. Values 1 and True are considered as the same thing and treated as duplicates

Sets can contain different data types

```bash
myfruits = {"apple", "banana", "cherry"}
print(myfruits)

# prints set length
print(len(myfruits))

# Acess items
for x in myfruits
  print(x)
```

## Set constructor

```bash
myfruits = set(("apple", "banana", "cherry")) # note the double round-brackets
print(myfruits)

# prints set length
print(len(myfruits))
```

## Add set Items

Use add() method

```bash
myfruits = set(("apple", "banana", "cherry")) 

myfruits.add("watermelon")
```

To add items from another set into the current set, use the update() method.

```bash
myfruits = set(("apple", "banana", "cherry")) 

matunda = {"ndizi","chungwa"}

myfruits.update(matunda)

```

Add any Iterable to a set 

The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

```bash
cars = set(("toyota","VW","mercedes")) 
JDM = ["subaru"]

myfruits.update(JDM)

```

## Remove Item

```bash
myfruits = set(("apple", "banana", "cherry")) 

myfruits.remove("apple")
```
If the item does not exist remove will raise an error. discard() does not raise an error.

pop() returns the removed item, but removes a random item.

```bash
myfruits = set(("apple", "banana", "cherry")) 

x = thisset.pop()
```

.clear() method empties the set
