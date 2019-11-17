Q Write a Python program to get unique values from a list.


p=['red', 'white', 'black', 'red', 'green', 'black']
length=len(p)
list1=[]
for i in range(length):
    for j in range(i+1,length):
        if p[i]==p[j] and p[i]!='$':
            p[j]='$'
    if p[i]!='$':
        list1.append(p[i])
print(list1)
