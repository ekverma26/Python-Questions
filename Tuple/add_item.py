Q Write a Python program to add an item in a tuple.

tup=(1,2,3)
l1=list(tup)
x=int(input("Enter number which you want to add:"))
l1.append(x)
tup1=tuple(l1)
print(tup1)
