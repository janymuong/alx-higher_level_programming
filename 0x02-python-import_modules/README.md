## `python`` - import & modules
---

> Notation: `import module_name`, `from module import submodule`, `import item.subitem.subsubitem` and a few others.

This is a directory for learning **Python imports** which basically allows you to use **functions**, **attributes**, and **variables**.
Modules could be files created for modularized coding - separation of concern, or modules could be from the standard library(packages).

A module is a file containing Python definitions and statements. 
The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable `__name__` which could be anything from Python `namespaces`.
Imports are normally included as top-level code.

Arbitrary example from the Python interpreter:
```bash
>>> from urllib.request import urlopen
>>> with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
...     for line in response:
...         line = line.decode()
...         if line.startswith('datetime'):
...             print(line.rstrip())
...
datetime: 2023-03-09T15:23:53.144247+00:00
```
