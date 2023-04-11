## `Python` - Inheritance

> `Inheritance` is an OOP mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class. It is the capability of one class to derive or inherit the properties from another class.

Allows for code reuse.	 	  

The syntax for a derived class definition looks like this - demo inheritance.

```bash
$ cat file.py
#!/usr/bin/python3
class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class Anime(Base):
    """ My User class """

    def __init__(self):
        super().__init__()
        self.id += 99

levi = Anime()
print(levi.id)
$ chmod +x file.py && ./file.py
$ 100
```
