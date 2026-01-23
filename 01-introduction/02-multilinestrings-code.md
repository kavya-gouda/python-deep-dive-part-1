# multiline statements and strings

how Python programs works

```
Python program
    -> Physical lines of code  (ends with physical  newline character)
        -> logical lines of code (ends with a logical new line token)
            -> tokenized
```

Physical newline vs logical newline

sometimes, physical newlines are ignored in order to combine multiple physical lines into a single logical lines of code terminted by a logical Newline token


machine doesn't care about readability, in python everything is going to be tokenized, but for us it should be readable

this conversion can be implicit or explicit, we will see what is implicit and explicit


### Implicit: 
    Expression enclosed by :
    [] - list literals, list comprehensive
    () - standard expressions, tuples
    {} - dictionary / set literals or comprehensions
    fucntional arguments/ parameters
    supports inlins comments

ex, 
```

[1, #item 1 
2, #item 2
3 #item 3
]

def my_func(a, 
b, #comment
c):
print(a, b, c)

my_func(10, #comment
20, 30)
```    

In the above cases, python interpreter is going to combine all those physical lines, to compile

### Explicit

You can break up statements over multiple lines explicitly, by using the \ (backslash ) character
Multi-line statements are not implicitly converted to a single logical line.

```
this is not going to work
if a 
and b
and c:

this will work

if a \
and b \
and c:
```

Comments cannot be part of a statement, not even a multi-line statement.

```
This will not work
if a \
and b \ #comment
and c:
```
## multi-Line strings Literals

Multi-line string literals can be created using triple delimiters (' single or " double)
'''This is
a multi-line string'''

"""This is
a multi-line string"""

Be aware that non-visible characters such as newlines, tabs, etc. are actually part of the string – basically anything you type.

You can use escaped characters (e.g. \n, \t), use string formatting, etc.
A multi-line string is just a regular string.
Multi-line strings are not comments, although they can be used as such,especially with special comments called docstrings.

![code snippet](imgs\image.png)


