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
