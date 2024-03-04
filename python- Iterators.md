## Python Iterators

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

Lists, tuples, dictionaries, strings and sets are all iterable objects. 

### IF loop
```bash
fruits = ("apple", "banana", "cherry")
myit = iter(fruits)

print(next(myit))
print(next(myit))
print(next(myit))

```

## Create an Iterator
Class to implement iter and stop when a is 20
```bash
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

```