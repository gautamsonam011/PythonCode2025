# Can we Pass a function as an argument in Python?

def add(a, b):
    return a+b

def apply_other_func(func, x, y):
    return func(x, y)

obj = apply_other_func(add, 4, 6)
print(obj)


# decorator 

# without decorator function 

def greet():
    print("Hello")

def logging_wrapper(func):
    def inner():
        print("Function is about to run") 

        func()
        print("Finished function")
    return inner

greet = logging_wrapper(greet)
greet()
    
# with decorator

def logging_wrapper_function(func):
    def wrapper():
        print("Function is about to run") 

        func()
        print("Finished function")
    return wrapper

@logging_wrapper_function
def greet():
    print("Hello") 

greet() 

def student(func):
    def wrapper():
        print("Hello!")
        func()
        print("Finished!")

    return wrapper

@student
def greett():
    print("This is Raju")

greett()


# What is a dynamically typed language?

# In a dynamically typed language, the data type of a variable is determined at runtime, not at compile time.
# No need to declare data types manually; Python automatically detects it based on the assigned value.
# Examples of dynamically typed languages: Python, JavaScript.
# Examples of statically typed languages: C, C++, Java.
# Dynamically typed languages are easier and faster to code.
# Statically typed languages are usually faster to execute due to type checking at compile time.

x = 10
print(type(x))







