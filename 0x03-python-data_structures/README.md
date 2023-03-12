## `python`: Data Structures - Lists, Tuples
---

Covers `sequence data types` - `lists`, and `tuples`.

> Def: 	  
> Lists are mutable sequences, typically used to store collections of homogeneous items (where the precise degree of similarity will vary by application).  	 
> Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples which could have lists). 

Also focuses (slightly or not slightly) on zero based indexing, slicing and generally lexicographical operations as a general approach to **sequence types**.


---
### CPython 

> compile and create a shared library:
```bash
$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c

$ ls
$ 100-print_python_list_info.c  100-test_lists.py  libPyList.so
```

> Test using a script:
```bash
$ cat 100-test_lists.py
import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
l = ['hello', 'World']
lib.print_python_list_info(l)
del l[1]
lib.print_python_list_info(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(l)
l = []
lib.print_python_list_info(l)
l.append(0)
lib.print_python_list_info(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list_info(l)
l.pop()
lib.print_python_list_info(l)
```

```bash
$ python3 100-test_lists.py
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: str
Element 1: str
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: str
[*] Size of the Python List = 7
[*] Allocated = 7
Element 0: str
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: str
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
$
```
		 
> **Note**		  
> Compilation, and Testing : `Ubuntu 14.04 LTS`, `Python 3.4`
