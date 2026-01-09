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
        print("This is Raju")
        func()
        print("Finished!")

@student
def call():
    print("Hello")

call()






