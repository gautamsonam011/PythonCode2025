# How are arguments passed by value or by reference in Python?

# Depending on the type of object you pass in the function, the function behaves differently. 
# Immutable objects show “pass by value” whereas mutable objects show “pass by reference”.

def call_by_value(x):
    x = x*5
    return x

def call_by_reference(b):
    b.append("D")
    return b

a = ["A", "B", "C"]

num = 34

updated_value = call_by_value(num)
updated_reference_value = call_by_reference(a)

print("Pass by value argument in function", updated_value)
print("Pass by reference in function", updated_reference_value)

