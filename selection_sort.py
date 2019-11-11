l=[]
n=int(input("enter size of list:"))
print("enter ",n," element:")
for i in range(0,n):
    x=int(input())
    l.append(x)
print("List: ",l)
for i in range(0,len(l)):
    m=i
    for j in range(i+1,len(l)):
        if l[m]>l[j]:
            m=j
    if min!=i:
        temp=l[i]
        l[i]=l[m]
        l[m]=temp
print(l)
