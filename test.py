def my_func(*args):
    """my doc on function"""
    return sum(args)

l = [1, 2, 3]
print(my_func(*l))

print(help(my_func))