l=[]
n=int(input("enter size of list:"))
print("enter ",n," element:")
for i in range(0,n):
    x=int(input())
    l.append(x)
print("List: ",l)
x=len(l)
for i in range(0,len(l)):
    for j in range(0,x-i-1):
        if l[j+1]<l[j]:
            a=l[j]
            l[j]=l[j+1]
            l[j+1]=a
print("Sorted list:",l)
