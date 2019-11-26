Q Write a Python program to access a function inside a function.


def add(a,b):
    c=a+b
    return c
def cal(a,b):
    d=a*b
    print(add(d,10))
cal(10,5)
