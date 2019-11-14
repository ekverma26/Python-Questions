Q Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

string=input("Enter a string:")
def fun(str):
    p=len(str)
    if p>=2:
        return (str[:2]+str[-2:p])
    else:
        return "Empty"
print(fun(string))
