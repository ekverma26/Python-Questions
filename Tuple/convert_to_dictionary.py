Q Write a Python program to convert a tuple to a dictionary.

tup=(1,2,3)
d={}
for i in range(len(tup)):
    d[i]=tup[i]
print(d)
