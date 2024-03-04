## Python Classes

```bash
Class car:
    make = 'Honda'

civic = Car()

print(civic.make)
```

use the __init__() function to assign values for name and age:

```bash
class Person:
  def __init__(self, name, age):
    self.f_name = name
    self.age = age

guy = Person("John", 36)

print(guy.name)
print(guy.age)

```
The __str__() function controls what should be returned when the class object is represented as a string.

```bash
class Human:
  def __init__(self, l_name, age):
    self.l_name = l_name
    self.age = age

  def __str__(self):
    return f"{self.l_name}({self.age})"

p1 = Person("Wanjema", 36)

print(p1)

```

Add a function to a class

```bash
class Human:

    def __init__(self, l_name, age):
        self.l_name = l_name
        self.age = age

    def __str__(self):
        return f"{self.l_name}({self.age})"

    def my_year_of_birth(self):
        return current_year - self.age

    

p1 = Person("Wanjema", 36)

print(p1)

yob = p1.my_year_of_birth()

print(yob)

## articles class
class Articles:
    '''
    News articles to define article Objects
    '''

    def __init__(self,id,name,title,url,urlToImage,content,publishedAt):
        self.id =id
        self.name = name
        self.title = title
        self.url = url
        self.urlToImage = urlToImage
        self.content = content
        self.publishedAt = publishedAt

```

