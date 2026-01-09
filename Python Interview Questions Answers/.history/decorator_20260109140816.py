# Can we Pass a function as an argument in Python?

def add(a, b):
    return a+b

def apply_other_func(func, x, y):
    return func(x, y)

obj = apply_other_func(add, 4, 6)
print(obj)