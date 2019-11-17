Q Write a Python program to split a list every Nth element.
Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]


l1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
a=[]
b=[]
c=[]
n=int(input("enter nth element:"))
for i in range(0,len(l1),n):
    a.append(l1[i])
for i in range(1,len(l1),n):
    b.append(l1[i])
for i in range(2,len(l1),n):
    c.append(l1[i])
t=[]
t.append(a)
t.append(b)
t.append(c)
print(t)
