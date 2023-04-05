## `Python` - Test-driven development

Covers the Python modules/frameworks: `doctest`, `unittest`

> Unittest uses methods created in classes(`unittest` is object-oriented) to manage tests. It has support for automation, setup, and shutdown code when testing. Unittest has several rich, in-built features that are unavailable in doctest, including generators and group fixture managers like setUp and tearDown.


> Doctest is an inbuilt test framework that comes bundled with Python by default. The doctest module searches for code fragments that resemble interactive Python sessions and runs those sessions to confirm they operate as shown.
> Developers commonly use doctest to test documentation. The doctest module looks for sequences of prompts in a docstring, re-executes the extracted command, and compares the output with the command’s input given in the docstrings test example.


### Test Context for `doctest`
The execution context created by doctest as it runs tests contains a copy of the module-level globals for the test module. Each test source (function, class, module) has its own set of global values to isolate the tests from each other somewhat, so they are less likely to interfere with one another.

Syntax for: Running Tests:
```bash
# example for doctest:
python3 -m doctest ./tests/*
# or for unittest:
python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1
```

## In doctests 
Option Flags:
	`NORMALIZE_WHITESPACE`, `ELLIPSIS`, `BLANKLINE` etc.
