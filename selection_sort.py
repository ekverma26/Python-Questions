l=[]
n=int(input("enter size of list:"))
print("enter ",n," element:")
for i in range(0,n):
    x=int(input())
    l.append(x)
print("List: ",l)

for i in range(0,len(l)):
    for j in range(0,len(l)):        
        if l[i]<l[j]:
            a=l[i]
            l[i]=l[j]
            l[j]=a
print("Sorted list:",l)
