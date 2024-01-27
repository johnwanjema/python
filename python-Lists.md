## Python Lists
Lists are used to store multiple items in a single variable. 
List items are ordered, changeable, and allow duplicate values.

```bash
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

A list can contain different data types:
```bash
list1 = ["abc", 34, True, 40, "male"]
print(list1)
```


## Python Collections (Arrays)
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

## Access List Items
List items are indexed and you can access them by referring to the index number:

```bash
list1 = ["abc", 34, True, 40, "male"]
print(list1[0]) # prints first element
```
Negative Indexing
Negative indexing means start from the end
-1 refers to the last item, -2 refers to the second last item etc.


By leaving out the start value, the range will start at the first item to index-1
list1[:3]

By leaving out the end value, the range will go on to the end of the list starts at the index to the end of the list.
list1[3:]

## List Comprehension
List Comprehension offers the shortest syntax for looping through lists:

```bash
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


newlist = [x for x in numbers if x != 1]
```

## List Methods
```bash
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
```