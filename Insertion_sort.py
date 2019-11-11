l=[]
n=int(input("enter size of list:"))
print("enter ",n," element:")
for i in range(1,n+1):
    x=int(input())
    l.append(x)
print("List: ",l)
x=len(l)
for i in range(1,x):
    j=i-1
    key=l[i]
    print(key)
    while(j>=0 and key<l[j]):
        l[j+1]=l[j]
        j=j-1
    l[j+1]=key
print("Sorted list:",l)
