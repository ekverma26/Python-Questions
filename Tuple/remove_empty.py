Q. Write a Python program to remove an empty tuple(s) from a list of tuples. 
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']


l1=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
l2=[]
for i in l1:
    if i!=():
        l2.append(i)
print(l2)
