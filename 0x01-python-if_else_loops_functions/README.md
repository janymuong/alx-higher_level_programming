## `python` - if/else, loops, functions
---
Directory for **Control Flow** in Python.	 

These covers how statements affect or control the execution of code or other statements wrapped within the execution of a block and in functions.

Control flow and operations are done on an iterable, that is, an object suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted. 

### sample concepts covered:
> `if/else`, `loops`, `statement grouping`, `functions`

Also, this covers elementary introduction to `Python` and its `syntax`. So,this is build up from the preceding directory [0x00-python-hello_world](../0x00-python-hello_world).

---
### `Appendix` 
`appendix` a - base bytcode:		
> **Note**	 
> The [function](./102-magic_calculation.py) `def magic_calculation(a, b, c)` does exactly the same as the following Python bytecode:
```bash
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```

`appendix` b - exact `bytecode`:
```bash
root@HP:/alx-SE/alx-higher_level_programming/0x01-python-if_else_loops_functions# python3
Python 3.8.10 (default, Nov 14 2022, 12:59:47)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import dis
>>> def magic_calculation(a, b, c):
...     '''function based off specified bytecode'''
...     if a < b:
...         return c
 elif c ...     elif c > b:
...         return a + b
...     else:
        ...         return a * b - c
...
>>> dis.dis(magic_calculation)
  3           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 COMPARE_OP               0 (<)
              6 POP_JUMP_IF_FALSE       12

  4           8 LOAD_FAST                2 (c)
             10 RETURN_VALUE

  5     >>   12 LOAD_FAST                2 (c)
             14 LOAD_FAST                1 (b)
             16 COMPARE_OP               4 (>)
             18 POP_JUMP_IF_FALSE       28

  6          20 LOAD_FAST                0 (a)
             22 LOAD_FAST                1 (b)
             24 BINARY_ADD
             26 RETURN_VALUE

  8     >>   28 LOAD_FAST                0 (a)
             30 LOAD_FAST                1 (b)
             32 BINARY_MULTIPLY
             34 LOAD_FAST                2 (c)
             36 BINARY_SUBTRACT
             38 RETURN_VALUE
             40 LOAD_CONST               1 (None)
             42 RETURN_VALUE
>>>
```
