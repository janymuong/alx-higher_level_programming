## `Python` - Everything is `object`
> we know for a fact that Python treats stuff as objects eg sequence types, classes of dtypes etc.

---
Base info for file `103*` answers.
```bash
$ cat int.py 
a = 1
b = 1
$
```

Reasoning:
> CPython implementation uses integer caching. Means that small integer values are cached and reused across the program. In this case, since the value of `a` and `b` is **1**, they both point to the same `cached int object` with value **1**. Therefore, only one int object is created for the both lines.


> **Note**  	 	  
> answer changed

---
Base info for `106*` response:
```bash
$ cat string.py 
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
$
```
Assuming we are using a CPython implementation of Python3 with default options/configuration:

How many string objects are created by the execution of the first line of the script? (106-line1.txt)  			  	  
`One` string object is created with value "SCHL".

How many string objects are created by the execution of the second line of the script (106-line2.txt)?  		  	 
`No` new string objects are created. The existing string object with value "SCHL" is referenced by both variables a and b.

After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)   		  
`Yes`, the string object pointed by a is deleted because a is a reference to the string object "SCHL" and it is deleted by the del statement.


After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt) 	 
`No`, the string object pointed by b is not deleted because b is just a reference to the string object "SCHL" which still exists in memory.


How many string objects are created by the execution of the last line of the script (106-line5.txt)  		  
`One` new string object is created with value "SCHL". The variable c is assigned to this new string object.
