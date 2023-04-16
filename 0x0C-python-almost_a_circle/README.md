## `Python` - Almost a circle

> This is a metaphorical `circle` project used as a review for select segments of the Python programming language - segments done prior to getting to this point.

Review of:
```bash
- imports
- exceptions
- class
- private attribute
- getter/setter, and decorators
- class methods
- static methods
- inheritance
- unittest - # unit testing
- read/write file - file I/O
- `*args` and `**kwargs` - for positional, arbitrary(and keyword) arguments
- serialization/deserialization (for context, formats: JSON, CSV, XML, YAML, Protocol buffers, MessagePack)
  				# focuses on JSON (de)serialization.
```

### File Hierarchy:
```bash
├── README.md - project documentation.
├── models/ - the main driver of the project.
│   ├── base.py - Includes base (class) models ; for subclassing/inheritance.
│   ├── square.py
│   ├── rectangle.py - object model for a rectangle
│   ├── _init__.py - pass
├── tests/test_models/ - directory for unit testing, test cases/test suites etc.
└── * miscellaneous
```
