# Identifier Names

Identifier names are  case sensitive, 
My_var and my_var are different identifier

must follow below rules
1. starts with underscore(_) and letter
2. followed with any number of underscores(_), letters(a-z, A-Z) or digits
3. cannot be in reserved words, like, Not, In, and

# conventions
1.This is a convention to indicate "internal use" or "private" objects
Objects named this way will not get imported by a statement such as : 
from module import *

```
_my_var - single underscore
```
2. Used to "mangle" class attributes – useful in inheritance chains
```
__my_var
```

3. Used for system-defined names that have a special 
meaning to the interpreter. 
Don't invent them, stick to the ones pre-defined by Python!

```
__my_var__
double underscore
__init__
x < y x.__lt__(y)
```

Other Naming conventions

from the PEP 8 Style Guide

1.  Packages :  short, all-lowercase names. Preferably no underscores. ex, utilities
2.  Modules : short, all-lowercase names. Can have underscores. ex, db_utils dbutils
3. Classes : CapWords (upper camel case) convention ex, BankAccount
4.  Functions : lowercase, words separated by underscores (snake_case). ex, open_account
5. Variables : lowercase, words separated by underscores (snake_case). ex, account_id
6. Constants : all-uppercase, words separated by underscores, ex, MIN_VAR

https://www.python.org/dev/peps/pep-0008/
This is a should-read!
A foolish consistency is the hobgoblin of little minds
(Emerson)
