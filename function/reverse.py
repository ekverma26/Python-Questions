Q Write a Python function to reverses a string if it's length is a multiple of 4.


def reverse(str1):
    len1=len(str1)
    if len1%4==0:
        print(str1[::-1])
    else:
        print("Length is not multiple of 4")
s=input("enter string:")
reverse(s)
