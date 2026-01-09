import math

num1 = 3.6
num2 = 3.98
res = math.floor(num1)
res1 = math.floor(num2)
print(res)
print("floor always in integer that given after decimal=>", res1)

c = math.ceil(num1)
c1 = math.ceil(num2)
print(c)
print("ceil always in integer round value", c1)

#  What is the difference between / and // in Python?

print("Double slash", 5//2)  # always provide floor integer value
print("Single slash", 5/2)

